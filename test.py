import random

with open("trait de personnalité.txt", "r", encoding="utf-8") as f:
    trait = f.read()
    trait = trait.split("\n")
    for i in trait:
        trait[trait.index(i)] = i.split(" / ")

def check_double(rep):
    for i in rep:
            if len(i)>1:
                for j in rep:
                    if i[1] in j and i[0] != j[0]:
                        rep.remove(i)
                        rep.append(random.choice(trait))
                        print("ok")
                        return check_double(rep)
    return rep

for i in range(1000):
    rep = [random.choice(trait) for i in range(3)]
    print(rep)
    rep = check_double(rep)
    print(rep)