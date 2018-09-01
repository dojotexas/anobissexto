def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    if ano % 100 == 0 and ano % 400 == 0:
        return True

    return False

