from ast import literal_eval
x=input("Enter a value: \n")
#only works in python 2.x:
# y = raw_input("Enter a value")
print(x)
print(type(literal_eval(x)))