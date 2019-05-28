import collections

#Q1
def q1(big_list):
    count = 0
    for i in big_list:
        for j in range(len(i)):
            count += i[j]
    return count


#Q2A
def hailstone(n):
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = n * 3 + 1
        yield n


#2B
generator = (i for i in hailstone(11))
for i in generator:
    print(int(i), end=' ')
print(" ")


#2C
class Gen:
    def __init__(self, data):
        self.num = data

    def __next__(self):
        if self.num == 1:
            raise StopIteration

        if self.num % 2 == 0:
            self.num = int(self.num / 2)
        else:
            self.num = int(self.num*3 + 1)

        return self.num

    def __iter__(self):
        return self


#Q3
def reachable(graph, node):
    c = collections.deque([node])
    list_set = [node]
    while c:
        node = c.popleft()
        for i in graph[node]:
            if i not in list_set:
                c.appendleft(i)
                list_set.append(i)
    return list_set


#Q5A
def q5a():
    i = 2
    print("id before:", id(i))
    i = 8
    print("id after:", id(i))


#5B
class mutableInt(int):
    def _init_(self, value):
        self.value = value

    def _call_(self, value):
        self.value = value

    def _str_(self):
        return str(self.value)


#Q7A
def q7(number_list):
    less_than = list(filter(lambda x: x < 12, number_list))
    sum = 0
    for i in less_than:
        sum = sum + (2 ** i)
    return sum


#7C
def get_max_camera(cameras):
    from functools import reduce
    return reduce(lambda x, y: x if x[1] > y[1] else y, cameras)


#7B
def get_max_rez(cameras):
    return cameras[get_max_camera(cameras)][1]



#test
#q2
for num in hailstone(5):
    print(num)

gen = Gen(5)
for i in gen:
    print(int(i), end=' ')
print(" ")

#q5
q5a()
i = mutableInt(5)
print("id before:", id(i))
i._call_(8)
print("id after:", id(i))

#q7
num_list = [1, 6, 17, 20]
print(q7(num_list))

