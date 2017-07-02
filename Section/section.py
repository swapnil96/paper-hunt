#! /usr/bin/env

import os
import nltk
import ../Process/pdf_to_text
from nltk.tokenize.texttiling import TextTilingTokenizer
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import SExprTokenizer

def main(doc):

    tar = os.getcwd() + "/Repo/PDF/" + doc
    txt = pdf_to_text.text(tar)

def text_tiling_section(doc):

    tt = TextTilingTokenizer()
    a = tt.tokenize(doc)
    return a

def plain_corpus_section(doc):

    w = PlaintextCorpusReader(os.getcwd() + "/Repo/Text/", doc)
    return w.paras()

def paran_sect(doc):

    a = SExprTokenizer(parens="()").tokenize(doc)
    return a

main("paper.pdf")
