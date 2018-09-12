def end_other(a, b):
    aa = a.lower()
    bb = b.lower()
    if aa.endswith(bb) or bb.endswith(aa):
        return True
    return False
