

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

s = word_count("this is a collection of words of nice words this is a fun thing it is")


for a, b in sorted(s.items()):
    print("{:<10} : {:<1} ".format(a, b))

