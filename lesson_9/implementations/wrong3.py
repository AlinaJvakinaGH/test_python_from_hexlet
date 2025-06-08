def fill(cil, value, begin=0, end=None):
    if end is None:
        end = len(cil)
    # Убедимся, что begin и end положительные и в пределах списка
    begin = max(0, begin)
    end = min(end, len(cil))
    for i in range(begin, end):
        cil[i] = value