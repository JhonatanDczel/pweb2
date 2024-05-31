def esEscalar(m):
    first = m[0][0]
    for i, row in enumerate(m):
        for j, item in enumerate(row):
            if (i == j and item != first) \
                or (i != j and item != 0):
                return False
    return True

