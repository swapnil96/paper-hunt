# This will parse the arguments and call all the helper functions.

# Currently provided functionalities.
# -p = Name of the topic.
# -f = Find related work papers.
    # -L = give the link to the paper Online/offline




# See for which papers it is mentioned in related work section

# Download files that cited it.
from Download import download
from Process import *
download.download(name)

# Process all the PDFs to text and find the related work section in all of them.
process.process_dir()

related_work.process_dir()

# Logic for checking if a PDF is mentioned in other in related work section.


