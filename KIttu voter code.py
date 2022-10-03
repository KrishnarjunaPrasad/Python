print("enter age ;")
age=int(input())
if age>= 18:
    print("you are eligible to vote")
if age < 18:
    print("you are not eligible to vote!")
    print("Are you ready to apply for voter id")
ready= int(input())
if ready <=23:
    print("Applied")
    print("voter Id send it to your adress")
else:
    print("Then Go and do your work!")
