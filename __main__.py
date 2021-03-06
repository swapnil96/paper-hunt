# This will parse the arguments and call all the helper functions.

# Currently provided functionalities.
# -p = Name of the topic.
# -f = Find related work papers.
    # -L = give the link to the paper Online/offline




# See for which papers it is mentioned in related work section

# Download files that cited it.
# from Download import download
from Section import related_work
from Section import reference
from Process import pdf_to_text
import re
import os 

# download.download(name)
name = "FICA"
# Logic for checking if a PDF is mentioned in other in related work section.
papers = os.listdir("paper-hunt/Repo/" + name)
for paper in papers:
    # Get the necessary sections
    text = pdf_to_text.text(name, paper)
    rw_sec = related_work.find_related(text)
    ref_sec = reference.find_reference(text)
    idx = re.findall('\[[^\]]*\]', rw_sec)
    for lis in idx:
        # Found related_work section
        temp = lis.split(',')
        num = []
        for t in xrange(len(temp)):
            if t == 0:
                tt = temp[t].split('[')
                if '-' in tt[1]:
                    ttt = tt[1].split('-')
                    num.append(int(ttt[0]))
                    num.append(int(ttt[1]))

                else:
                    ttt = tt[1].split(']')
                    num.append(int(ttt[0]))

            elif t == len(temp) - 1:
                tt = temp[t].split(']')
                if '-' in tt[1]:
                    ttt = tt[1].split('-')
                    num.append(int(ttt[0]))
                    num.append(int(ttt[1]))

                else:
                    num.append(int(tt[0]))

            else:
                if '-' in temp[t]:
                    ttt = temp[t].split('-')
                    num.append(int(ttt[0]))
                    num.append(int(ttt[1]))

                else:
                    num.append(int(temp[t]))

        for n in num:
            try:
                ref = ref_sec[n]
                if name in ref:
                    ans.append(paper)

            except:
                pass    
            
    print 'adsf'