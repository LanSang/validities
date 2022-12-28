import sys
import random


def read_sents(fn):
    sents = []
    sent = []
    with open(fn, "r") as inf:
        for i in inf:
            if i == "\n":
                sents.append(sent)
                sent = []
            else:
                sent.append(i)
                
    return sents
   
def write_only_products(sents, fnout):
    c = 0
    with open(fnout, "w") as of:
        for sent in sents:
            tags = set(o.replace("\n", "").split('\t')[1] for o in sent)
            if tags == set(["O"]):
                if random.random() < .1:
                    for o in sent:
                        of.write(o)
                    of.write('\n')
                    c += 1
            if tags == set(["I-product", "B-product", "O"]):
                for o in sent:
                    of.write(o)
                of.write('\n')
                c += 1
    sys.stderr.write(f"wrote {c}\n")


if __name__ == "__main__":   
    fn = "wnut/wnut16/data/dev.conll"     
    fnout = "wnut/wnut16/data/dev.products.conll"            
    sents = read_sents(fn)
    write_only_products(sents, fnout=fnout)

    fn = "wnut/wnut16/data/train.conll"     
    fnout = "wnut/wnut16/data/train.products.conll"            
    sents = read_sents(fn)
    write_only_products(sents, fnout=fnout)