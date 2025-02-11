strs = ["eat","tea","tan","ate","nat","bat"]

a = {}
for i in strs:
    s = ''.join(sorted(i))
    if s in a:
        a[s].append(i)
        print(a)
    else:
        a[s] = [i]

print(list(a.values()))