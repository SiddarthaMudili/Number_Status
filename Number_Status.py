#Prime_or_Composite
#Python Program Which Finds out whether a number in a given range is Prime or Composite
A=int(input("Enter lowest number of the Range: "))
B=int(input("Enter Highest Number of the Range: "))
length=B-A
print("In the Range of Numbers","["+str(A)+","+str(B)+"]")
for num in range(A,B+1):
    flag = False #num is a Prime number
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                flag=True #num is a Composite number
    if flag:
        print(num,"is Composite Number")
    else:
        count=0
        if num>=0:
            if num==1 or num==0:
                print(num,"Neither Prime Nor Composite") #Since 1 and 0 are neither prime nor composite
            else:
                print(num,"is Prime Number")
                count+=1
        else:
            print("Invalid Input")
            print("Negative integers are not considered")
            break
count_p=0 #Number of Prime numbers
length=B-A+1 #Length of the Range
for num in range(A,B+1):
    if num<=1:
        length-=1
        continue
    for i in range(2,num):
        if(num%i)==0:
            break
    else:
        count_p+=1
count_c=length-count_p #Number of Composite numbers
print("Count:\n",count_p,"Prime numbers and",count_c,"Composite numbers are in the Range") #Count of Prime and Composite numbers