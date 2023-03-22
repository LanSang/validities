import json

import spacy
from tqdm import tqdm
from spacy.lang.en import English

class Sentencizer(object):
    def __init__(self) -> None:
        self.nlp = English()
        self.nlp.add_pipe("sentencizer")

    def sentencize(self, text):
        sentences = []
        doc = self.nlp(text)
        for sent in doc.sents:
            sentences.append(sent.text)
        return sentences

if __name__ == "__main__":
    sn = Sentencizer()
    for _ in sn.sentencize("I love to bike. I use the radpower4."):
        print(_)