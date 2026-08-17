# 4
students = [
 {"name": "Sara", "score": 92, "attendance": 0.95},
 {"name": "Ali", "score": 67, "attendance": 0.60},
 {"name": "Omid", "score": 85, "attendance": 0.88},
 {"name": "Neda", "score": 74, "attendance": 0.99},
 {"name": "Reza", "score": 55, "attendance": 0.70},
]
from functools import reduce
a = list(filter(lambda i: i["score"]>70 and i["attendance"]>0.8,students))
b = sorted([(s["name"] , s["score"]) for s in a],key= lambda i: i[1],reverse=True)
c  = {i[0] : i[1] for i in b}
d = list(map(lambda item: min(item + 5, 100), c.values()))
e = reduce(lambda x,y: x + y,d)
total = e / len(d)

final_list = list(map(lambda item: (item["name"] , min(item["score"]+5,100)),a))

def final(x):
    for i in x:
        yield i[0] , i[1]

for i,j in final(final_list):
    print(f"{i}: {j:.2f}" )
