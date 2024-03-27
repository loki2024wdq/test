
a = [(1,2),(3,4),(5,6)]
n={2:None}
f = [(q,w,t) for (q,w) in a if w not in n for t in range(3)]
print(f)