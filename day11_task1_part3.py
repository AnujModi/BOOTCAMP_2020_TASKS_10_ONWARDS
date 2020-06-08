def type_checker(x):
    try:
        val = int(x)
        print("Number " + x + " is an integer")
    except ValueError:
        try:
            val = float(x)
            print("Number " + x + " is an floating point type")
        except ValueError:
            print(x + " is a String type")
x=input("Enter any number between 1 and 10: ")
if int(float(x)) <= 10 and int(float(x)) >= 1:
    y = input("Enter another number between 1 and 10: ")
    if int(float(y)) <= 10 and int(float(y)) >= 1:
        z = int(float(x))+int(float(y))
        print(z+30)
    else:
        print("enter a number between 1 and 10... rerun now")
else:
    print("enter a number between 1 and 10... rerun now")
type_checker(x)
type_checker(y)
#since i have defined a function, everytime the function is invoked, it will check the real time value of the type...
#hence yea... everytime my type value will change, once type of the input is changed as well...