
def mutate_string(s, p, c):
    l = list(s)
    l[p] = c
    return ''.join(l)

