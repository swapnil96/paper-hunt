
import re
import os
import sys
import ref_list

def find_reference(doc):

    match1 = [(m.start(0), m.end(0)) for m in re.finditer("REFERENCES", doc)]
    match2 = [(m.start(0), m.end(0)) for m in re.finditer("REFERENCE", doc)]
    match3 = [(m.start(0), m.end(0)) for m in re.finditer("References", doc)]
    match4 = [(m.start(0), m.end(0)) for m in re.finditer("Reference", doc)]

    if match1 != []:
        new = doc[match1[-1][1]:]

    elif match2 != []:
        new = doc[match2[-1][1]:]

    elif match3 != []:
        new = doc[match3[-1][1]:]

    elif match4 != []:
        new = doc[match4[-1][1]:]

    refs = ref_list.main(new)
    # f = open("../Repo/FICA/paper.txt", "w")
    # for ref in refs:
    #     f.write(ref)
    #     f.write("\n")

    # f.close()
    return refs
