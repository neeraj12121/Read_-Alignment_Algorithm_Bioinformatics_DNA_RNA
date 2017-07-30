
def data_read(filename):
    l = ''
    f = open(filename)
    for line in iter(f):
            if not line[0] == '>':
                l += line.rstrip()
    f.close()
    return l


