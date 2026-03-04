# def circledata(r):
#     circumference =2*3.14*r
#     area = 3.14*r*r
#     return circumference,area

# print(circledata(5))



def first (num):
    print(num)
    def second(x):
        return x**num
    return second

f=first(2)
print(f(4))
