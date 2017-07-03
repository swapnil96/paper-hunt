
# from paper_hunt.Section import section
from ..paper_hunt import Section

pri_matches = {"RELATED WORK": 10, "RELATED": 7, "SIMILAR": 9, "SIMILAR WORK":9, "Similar work": 10, "similar work":8, "related work":8, "Related work":10}
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


# def process_dir(name):

