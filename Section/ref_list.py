
import re

# Return references from document in a list

def first_option(doc):

    pattern = re.compile('\[[0-9]+\]')
    ref = []
    pos = []
    for refs in pattern.finditer(doc):
        pos.append(refs.start())

    for p in xrange(len(pos) - 1):
        s = doc[pos[p]:pos[p+1]]
        s = s.replace('\n', " ")
        ref.append(s)

    return ref

def second_option(doc):

    pattern = re.compile('\\\n[0-9]+\.')
    ref = []
    pos = []
    for refs in pattern.finditer(doc):
        pos.append(refs.start())

    for p in xrange(len(pos) - 1):
        s = doc[pos[p]:pos[p+1]]
        s = s.replace("\n", " ")
        ref.append(s)

    return ref

def thrid_option(doc):

    pattern = re.compile('\.\\\n[A_Z]+')
    ref = []
    pos = []
    for refs in pattern.finditer(doc):
        pos.append(refs.start())

    for p in xrange(len(pos) - 1):
        s = doc[pos[p]:pos[p+1]]
        s = s.replace("\n", " ")
        ref.append(s)

    return ref


def fourth_option(doc):

    length = len(doc)
    last = 0
    ref = []
    for index in xrange(length):

        if doc[index] == '\n':
            if doc[index-1] == '.' or doc[index+1].isupper() == True:
                s = doc[last:index]
                s = s.replace("\n", " ")
                s = s + "\n"
                ref.append(s)
                last = index + 1

    return ref

def main(doc):

    result = first_option(doc)
    if result != []:
        return result

    result = second_option(doc)
    if result != []:
        return result

    result = thrid_option(doc)
    if result != []:
        return result

    result = fourth_option(doc)
    return result
