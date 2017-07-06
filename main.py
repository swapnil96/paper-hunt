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
import re
import os 

# download.download(name)
name = "FICA"
# Logic for checking if a PDF is mentioned in other in related work section.
papers = os.listdir("Repo/" + name)
for paper in papers:
    # Get the necessary sections
    rw_sec = related_work.find(paper)
    ref_sec = reference.find(paper)
    lis = re.findall('\[[^\]]*\]', sec)
    if lis:
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
                    num.append(int(tt[1]))

            elif t == len(temp) - 1:
                tt = temp[t].split(']')
                if '-' in tt[1]:
                    ttt = tt[1].split('-')
                    num.append(int(ttt[0]))
                    num.append(int(ttt[1]))

                else:
                    num.append(int(tt[1]))

            else:
                if '-' in temp[t]:
                    ttt = temp[t].split('-')
                    num.append(int(ttt[0]))
                    num.append(int(ttt[1]))

                else:
                    num.append(int(temp[t]))

        for n in num:
            ref = ref_sec[n]
            if name in ref:
                ans.append(paper)
        
