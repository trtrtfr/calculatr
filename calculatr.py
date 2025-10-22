a=int(input("enter the first number "))
b=int(input("enter the first number "))
operation=input("+,-,*,/ \n")
if operation=="+":
    c=a+b
    print(c)
elif operation=="-":
    c=a-b
    print(c)
elif operation=="*":
    c=a*b
    print(c)
elif operation=="/":
    if b==0:
        print("invalid")
    else:
        c=a/b
        print(c)
