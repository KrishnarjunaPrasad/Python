print("Enter your marks")
marks = int(input())
if marks <=35:
    print("Sorry your are Failed Exam. Better luck Next time!!", marks)
elif marks >35:
    print("passed")
    if marks >75 and marks <= 85:
        print("You Got Good Marks", marks)
    elif marks >85 and marks <95:
        print("Great Marks")
    elif marks >95 and marks<100:
        print("Topper")
    else:
        print("Keep work hard")
else:
    print("Congratulations! You are Passed~!", marks)
    
