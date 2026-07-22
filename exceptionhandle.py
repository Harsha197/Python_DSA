# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("done")
# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else:
#     print("done")
# try:
#     a=int(input("Enter a number: "))
#     print(a)
# except ValueError as e:
#     print(e) 
# else:
#     print("done")   
# a=int(input("Enter a number: "))
# if a<0:
#     raise ValueError("Number is negative")
# else:
#     print(a)
#Task-2

# try:
#     l=[1,2,3,4,5,6,7,8,9,10]
#     print(l[10])
# except IndexError as i:
#     print(i)
# finally:
#     print("done")   

# try:
#     a=int(input("Enter a Number"))
#     while a>0:
#         print(a)
# except ValueError as e:
#     print(e)
# finally:
#     print("Done")

# try:
#     a=int(input("Enter a number"))
#     while a>0:
#         print(a)
#         a-=1
# except ValueError as e:
#     print(e)
# finally:
#     print("Done")

while True:
    try:
        a=int(input("Enter a number"))
        while a>0:
            print(a)
            a-=1
    except ValueError as e:
        print(e)
    finally:
        print("Done")
        