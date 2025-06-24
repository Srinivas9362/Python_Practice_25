def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Invalid Number")

print(round(divide(10,3),3))

divide(20,0)