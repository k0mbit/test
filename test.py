#This is a test
print("Testing 1 2 3")

#I learned about dictionaries and * ** expansion today
letters = {"A" : 1,
    "B" : 2,
    "C" : 3}

letters2 = {"D" : 4,
    "E" : 5,
    "F" : 6}

#Originall I put the letters where the numbers are but that threw an error
letters_all = {**letters, **letters2}

#If I just do this it doesn't format well
print(letters_all)

#Def a function MDC (Magic Dictionary Combiner)
def mdc(**kwargs):
    for key in kwargs:
        print(str(key) + " " + (str(kwargs[key])))

mdc(**letters_all)

#Prints randomly so let's try Stuff
print(sorted(**letters_all))
# TypeError "Sorted only takes 3 arguments"

sorted(mdc(**letters_all))
# TypeError "Object is not iterable"

mdc(sorted(**letters_all))
# TypeError: mdc() takes 0 positional arguments but 1 was given
