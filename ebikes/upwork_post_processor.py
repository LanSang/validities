import requests
import re
import spacy
from spacy.lang.en import English
from bs4 import BeautifulSoup
import gzip
import json  
import docxpy
import numpy as np
from dataclasses import dataclass
from numpy import ndarray
from typing import List
from colorama import Fore
from sentence_transformers import SentenceTransformer
from colorama import Style


def get_ngrams(tokens, n=2):
    return [" ".join(o) for o in zip(*[tokens[i:] for i in range(n)])]


class Spacy(object):

    def __init__(self, model = "en_core_web_sm"):
        self.nlp = spacy.load(model)

    def tokenize(self, text):
        doc = self.nlp(text)
        tokens = [str(t) for t in doc]
        return tokens

    def sentence_split(self, text):
        '''this seems to be too restrictive for reddit comments'''
        return [str(i) for i in self.nlp(text).sents]

class DocX(object):

    @staticmethod
    def get_links(file = 'demo.docx'):

        # extract text
        text = docxpy.process(file)

        # if you want the hyperlinks
        doc = docxpy.DOCReader(file)
        doc.process()  # process file
        hyperlinks = doc.data['links']

        return hyperlinks


class Reddit(object):

    def __init__(self, filename="ebikes.RC_2022-10.gz"):
        '''Stuff from reddit in jsonl format'''
        self.filename = filename

    def get_comments_for_link_id(self, link_id):
        out = []
        with gzip.open(self.filename,'rb') as fin:        
            for line in fin:   
                line = line.decode()
                line = json.loads(line)
                if line["link_id"].endswith(link_id):
                    out.append(line)
        return out

    @staticmethod
    def get_comments_mentioning_product(comments, product):
        out = []
        for o in comments:
            if product in o["body"]:
                out.append(o["body"])
        return out


@dataclass
class WebpageText:
    url: str
    page_text: str
    page_sentences: List[str]
    sentence_embeddings: ndarray


class WebpageFactory(object):

    def __init__(self, spacy, sbert):
        self.spacy = spacy
        self.sbert = sbert

    def make_webpage(self, url='https://yubabikes.com/cargobikestore/mundo-electric/'):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.text.replace("\n", " ").replace("\t", " ").strip()
        text = re.sub(' +', ' ', text)
        page_sentences = list(self.spacy.sentence_split(text))
        page_sentence_embeddings = sbert.encode(page_sentences)
        return WebpageText(url, text, page_sentences, page_sentence_embeddings)


@dataclass
class ProductMention:
    comment_containing_mention: str
    sentence_containing_mention: str


if __name__ == "__main__":
    docx = DocX()
    hyperlinks = docx.get_links()
    links = hyperlinks[5:9]

    sbert = SentenceTransformer('all-MiniLM-L6-v2')
    reddit = Reddit()

    print('\033[39m')
    print(Fore.RED + 'Warning: The post yaz4wv is hard coded.')
    print(Fore.YELLOW + 'Idea: To validate work, see if they get the same links as included in post.')
    print(Fore.WHITE + "")

    comments_for_link = reddit.get_comments_for_link_id("yaz4wv")

    spacy = Spacy()
    factory = WebpageFactory(spacy=spacy,
                             sbert=sbert)

    for product, url in links[1:]:

        webpage = factory.make_webpage(url)
        product = product.decode()
        comments_about_product: List[str] = reddit.get_comments_mentioning_product(comments_for_link, product=product)
        
        comment_sentence_embeddings = sbert.encode(comments_about_product)

        if len(comments_about_product) > 1:
            sims = comment_sentence_embeddings.dot(webpage.sentence_embeddings.T)
            sorted_ix = np.argsort(sims, axis=1) # get top 5 most similar
            
            for commentno, comment in enumerate(comments_about_product):
                ranked_sents = sorted_ix[commentno][-5:]
                print("***")
                print(Fore.GREEN + "reddit:" + Fore.WHITE + comment)
                for r in ranked_sents:
                    print(webpage.page_sentences[r])
    print(Fore.YELLOW + 'Idea: Also check bigram overlap')

