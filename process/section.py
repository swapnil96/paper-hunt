#! /usr/bin/env

import string
import pdf_to_text
import re
import os
import sys
import section
import nltk
from nltk.tokenize import SExprTokenizer
import sent
from nltk.tokenize import sent_tokenize
import ref_sent
import parts_of_speech

reload(sys)
sys.setdefaultencoding('utf8')

pri_matches = {"RELATED WORK": 10, "RELATED": 7, "SIMILAR": 9, "SIMILAR WORK":9, "Similar work": 10, "similar work":10, "related work":10, "Related work":10}
sec_matches = {"Introduction": 5, "introduction": 3, "Conclusion": 5, "conclusion": 3, "related": 4}

def find_related(doc):

    first_list = section.text_tiling_section(doc)
    pri_paras = []
    pri_paras_conti = []
    sec_paras = []
    total_length = 0

    for para in first_list:
        temp_length = len(para)
        total_length += temp_length
        got = 0
        for pat in pri_matches:
            match = [(m.start(0), m.end(0)) for m in re.finditer(pat, para)]
            if match != []:
                got = 1
                pri_paras.append([para, pat, total_length - temp_length, total_length])

            elif got == 1:
                got = 0
                pri_paras_conti.append([para, pat, total_length - temp_length, total_length])

    total_length = 0
    if pri_paras == []:
        for para in first_list:
            temp_length = len(para)
            total_length += temp_length
            for pat in sec_matches:
                match = [(m.start(0), m.end(0)) for m in re.finditer(pat, para)]
                if match != []:
                    sec_paras.append([para, total_length - temp_length, total_length])

    # for para in pri_paras:
    #     a = nltk.sent_tokenize(para[0])
    #     t = section.paran_sect(para[0])
    #     for j in t:
    #         if j[0] == "[" or j[0] == "(":
    #             print j
    #
    #     print '----------------------------------------------------------------------'
    #     for j in a:
    #         print j

def find_reference(doc):

    match1 = [(m.start(0), m.end(0)) for m in re.finditer("REFERENCES", doc)]
    match2 = [(m.start(0), m.end(0)) for m in re.finditer("REFERENCE", doc)]
    match3 = [(m.start(0), m.end(0)) for m in re.finditer("References", doc)]
    match4 = [(m.start(0), m.end(0)) for m in re.finditer("Reference", doc)]

    if match1 != []:
        new = doc[match1[-1][1]:]
        # sent_tokenize_list = sent_tokenize(new)

    elif match2 != []:
        new = doc[match2[-1][1]:]

    elif match3 != []:
        new = doc[match3[-1][1]:]

    elif match4 != []:
        new = doc[match4[-1][1]:]

    refs = ref_sent.main(new)
    f = open("Repo/Reference/paper.txt", "w")
    for ref in refs:
        f.write(ref)
        f.write("\n")

    f.close()


if __name__ == "__main__":
    t = pdf_to_text.text(os.getcwd() + "/Repo/PDF/paper.pdf")
    # find_related(t)
    find_reference(t)
