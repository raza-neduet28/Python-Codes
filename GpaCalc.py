b= float(input("Enter Number of courses :"))

a=1.0
sum=0.0
gpa=0
while b>=a:
    n = float(input("Enter GPA OF Subject :"))
    a=a+1
    m = float(input("Enter Credit hrs :"))

    gpa=gpa+(n*m)
    sum=sum+m
    
print("YOUR GPA IS  :",gpa/sum)