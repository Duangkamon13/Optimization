def rational_decision(s, p):
    is_confess_better_if_other_not_confess = s[p][1][0] < s[p][0][0]
    is_confess_better_if_other_confess = s[p][1][1] < s[p][0][1]
    if is_confess_better_if_other_not_confess and is_confess_better_if_other_confess:
        return 1 
    is_not_confess_better_if_other_not_confess = s[p][0][0] < s[p][1][0]
    is_not_confess_better_if_other_confess = s[p][0][1] < s[p][1][1]
    if is_not_confess_better_if_other_not_confess and is_not_confess_better_if_other_confess:
        return 0
    
if __name__ == '__main__':
    choices = ['not confess', 'confess']
    s = {'Lobha': [[3, 10], [1, 5]], 'Raga': [[3, 10], [1, 5]]}
    p = 'Lobha'
    r = rational_decision(s, p)
    print(p, ':', choices[r])