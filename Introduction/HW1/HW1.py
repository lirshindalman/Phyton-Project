def q1(big_list):
    count = 0
    for i in big_list:
        for j in range(len(i)):
            count += i[j]
    return count


def q2a(string1):
    print(string1[::-1])
    return


def q2b(list1):
    for i in range(len(list1)):
        if type(list1[i]) is list:
            list1[i].reverse()
    list1.reverse()
    return list1


def q2c(tup):
    return tup[::-1]


def q3a(tup1):
    temp = []
    for i in tup1:
        temp = i.union(temp)
    numbers = sorted(set(filter(lambda split: type(split) is int, temp)))
    flo = sorted(set(filter(lambda split: type(split) is float, temp)))
    letters = sorted(set(filter(lambda split: type(split) is str, temp)))

    sort1 = letters + sorted(numbers + flo)
    return sort1


def q3b(tub2):
    list5 = q3a(tub2)
    dictionary1 = {}
    for i in range(len(list5)):
        dictionary1.update({i: list5[i]})
    return dictionary1


def q6():
    #a
    x = int(input("pleas enter a number"))
    y = x > 10 and 6 or 9
    print(y)
    #b

    y = 6 if x > 10 else 9
    print(y)


def q7a():

    #a
    list3 = []
    x = int(input("pleas enter a number"))
    y = int(input("pleas enter a number"))

    x = x % 2 == 0 and x or x+1
    for i in range(x, y+1, 2):
        print(i)
        list3.append(i)
    for j in range(len(list3)):
        print(list3[len(list3)-j-1])

    #b
    list4 = []
    while x < y+1:
        print(x)
        list4.append(x)
        x = x+2
    z = 0
    while z < len(list4):
        print(list4[len(list4) - z - 1])
        z += 1


list2 = [[12, 4], [1], [2, 3]]
tuple1 = (1, 2, 4, 5)
tuple2 = ({1, 4, 'f', 6}, {4, 'y', 'r', 'A', 3})
print(q1(list2))
print(q2b(list2))
print(q2c(tuple1))
print(q3a(tuple2))
print(q3b(tuple2))
q6()
q7a()
