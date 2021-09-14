def increase(num):
    print(id(num))
    num+=1
    print(id(num))

a = 10    # using immutable type (int) so it cannot point to same object when increase
print(id(a))
increase(a)
print(a)


def increase_mutable(num):
    print(id(num))
    num[0]+=1
    print(id(num))


b = [10]    # using immutable type (list) so it will point to same object when increase
print("b",id(b))
increase_mutable(b)
print(b)

