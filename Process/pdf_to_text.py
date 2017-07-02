#! /usr/bin/env

import textract # Module for parsing the pdf as a text document
import os

def text(doc):

    if not os.path.exists("../Repo/Text"):
        os.makedirs("../Repo/Text")

    name = doc.split("/")
    name = name[-1].split(".")
    target = os.path.join(os.getcwd() + "../Repo/Text/", name[0] + ".txt")

    if os.path.isfile(target): # Checks if the file is already present
        with open(target, "r") as myfile:
            return myfile.read()

    text = textract.process(doc, encoding = "ascii") # Text is stored in text variable
    f = open(target, "w")
    f.write(text)
    f.close()
    return text

if __name__ == "__main__":
    text(raw_input("Name of the file(e.g - paper.pdf):"))
