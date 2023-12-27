import sys
import pandas as pd

F = set()
R = list()
G = set()

ans_r = list()
ans_T = list()
ans_S = list()
ans_R = list()

def loc(rules: list, fact: set) -> list:
    ans = list()
    for [left, right, id] in rules:
        if left.issubset(fact):
            ans.append([left, right, id])
    return ans

def getId(rules: list) -> list:
    ans = list()
    for [left, right, id] in rules:
        ans.append(id)
    return ans

def ForwardReasoning():
    T = F.copy()
    S = loc(R, F)

    ans_r.append(['', '', ''])
    ans_T.append(list(T))
    ans_S.append(S.copy())
    ans_R.append(R.copy())

    while (not G.issubset(T)) and (len(S) > 0):
        r = S.pop(0)
        T = T.union(r[1])
        R.remove(r)
        S = loc(R, T)
        
        ans_r.append(r.copy())
        ans_T.append(T.copy())
        ans_S.append(S.copy())
        ans_R.append(R.copy())
    
    if G.issubset(T):
        print('G đúng')
    else:
        print('G sai')

if __name__ == '__main__':
    sys.stdin = open('data.inp', 'r')
    
    n = int(input())
    F = set(input().split())
    for i in range(n):
        rule = list(map(lambda s: s.strip(), input().split('->')))
        rule[0] = set(rule[0].split())
        rule[1] = set(rule[1].split())
        rule.append('r' + str(i + 1))
        R.append(rule)
    G = set(input().split())
    
    data = {
        'r': [],
        'T': [],
        'S': [],
        'R': []
    }
    
    ForwardReasoning()
    len = len(ans_S)
    for i in range(len):
        data['r'].append(ans_r[i][2])
        data['T'].append(sorted(list(ans_T[i])))
        data['S'].append(getId(ans_S[i]))
        data['R'].append(getId(ans_R[i]))
    
    df = pd.DataFrame(data)
    print(df)