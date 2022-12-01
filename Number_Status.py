#write a program which finds whether a number is prime or composite
A=int(input("Enter lowest number of the Range: "))
B=int(input("Enter Highest Number of the Range: "))
print("In the Range of Numbers","["+str(A)+","+str(B)+"]")
for num in range(A,B+1):
    flag = False
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                flag=True
                break
    if flag:
        print(num,"is Composite Number")
    else:
        if num>0:
            if num==1:
                print(num,"Neither Prime Nor Composite")
            else:
                print(num,"is Prime Number")
        else:
            print("Invalid Input")
            break
