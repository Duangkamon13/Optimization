
def perf_note(pnotes, coefficient):
    for note in pnotes:
        name = note[0]
        min_coef = note[1]
        max_coef = note[2]
        if coefficient >= min_coef:
            if coefficient <= max_coef:
                return name

pnotes = [['head note', 1, 14],
['heart note', 15, 60],
['base note', 61, 100]]
note = perf_note(pnotes,8)
print(note)
note = perf_note(pnotes,34)
print(note)
note = perf_note(pnotes,78)
print(note)