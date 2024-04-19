from itertools import product

n = []
m = []
break_ = 0
times = 6
number = 20
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
def add2(place1, place2):
    if place1 - place2*2 < number and place1 - place2*2 not in n and place1 - place2*2 >0:
        n.append(place1 - place2*2)
    if place1 - place2 > 0 and place1 - place2 not in n:
        n.append(place1 - place2)
    if number - place1 - place2 > 0  and number - place1 - place2 not in n:
        n.append(number - place1 - place2)
        print(n)
for j in range(1, number + 1):
    m.append(j)
for d1 in m:
    if break_ == 1:
        break
    for d2 in m:
        if break_ == 1:
            break
        for d3 in m:
            if break_ == 1:
                break
            add(d1)
            add(d2)
            add(d3)
            add2(d1,d2)
            add2(d1,d3)
            add2(d2,d1)
            add2(d3,d1)
            add2(d2,d3)
            add2(d3,d2)
            k = [d1, d2, d3] 
            if set(n).issubset(m) == True and len(n) >= number - 1:
                print('FINISHED!')
                print(k)
                break_ = 1
                break
            else:
                print(n)
                n = []
print('NOTHING')
print(n)
