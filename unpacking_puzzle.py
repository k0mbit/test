#p1
print(2 * 3 + 2 ** 3)
#14

#p2
lst = [2468] * 5
print(lst)
#2468, 2468, 2468, 2468, 2468

#p3
def average(*args):
    return sum(args) / len(args)

print(average(13.0, 14.0, 15.0, 14.0))
#14.0

#p4
def likes(**kwargs):
    for key in kwargs:
        print(key + " likes " + kwargs[key])

likes(Alice="Bob", Bob="Ann")
#Bob likes Ann \n Alice likes Bob

#p5
dic = {"Alice" : "Ann",
        "Ann" : "Bob"}
likes(**dic)
#Ann likes Bob \n Alice like Ann

#p6
income_1 = {"Alice" : 1988,
            "Bob" : 2253}

income_2 = {"Pete" : 1324,
            "Frank" : 1474}

income = {**income_1, **income_2}
print(income)
#{'Bob': 2253, 'Alice': 1988, 'Pete': 1324, 'Frank': 1474}
