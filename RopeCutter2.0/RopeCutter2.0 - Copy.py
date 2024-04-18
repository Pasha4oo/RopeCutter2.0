from itertools import product

n = []
m = []
k = []
break_ = 0
times = 6
many_dict = []
number = 13
dict1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def add(place):
    if place not in n and place > 0 and place <= number:
        n.append(place)
        if place*2 <= number and place*2 not in n:
            n.append(place*2)
        if number - place*2 > 0 and number - place*2 not in n:
            n.append(number - place*2)
        if number - place > 0  and number - place not in n:
            n.append(number - place)
        print(n)
for j in range(1, number):
    m.append(j)
    many_dict.append([o for o in range(1, number + 1)])
while set(n).issubset(m) == False or n == [] and break_ == 0:
    for d1 in product(dict1, dict1, dict1, dict1, dict1, dict1, dict1, dict1, dict1, dict1, dict1, dict1):
        d1 = set(d1)
        if break_ == 1:
            break
        for f in d1:
            k.append(f)
            add(f)
            if set(sorted(m)).issubset(sorted(n)) == True and m != []:
                print('FINISHED!')
                break_ = 1
                break
            if len(k) >= times:
                n = []
                m = []
                k = []
    if break_ == 1:
        break
print(n)
print(k)