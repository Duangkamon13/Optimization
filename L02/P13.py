
def est_prob(counting):
    total = sum(counting)
    result = []
    for count in counting:
        prob = count / total   
        result.append(prob)     
    return result

counting = [0, 8, 20, 4, 12]
res = est_prob(counting)
print(res)
