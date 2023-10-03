t=0
try :
    n = int(input("Insert number here: "))
    if n!=0 :
        while True:
            print (n) #This is the actual 3x+1 part
            if n%2==1 :
                n= 3*n+1
            else :
                n= n/2
            t+=1
            if n==1 or n==-1 or n==-10 or n==-34: #To prevent infinite loops by breaking it if it reaches the end of a loop
                print(n)
                break
    elif n==0:
        print(0.0)
        t=1
    print ()
    print ("steps taken:")
    print (t)
except ValueError:
    print("Only integers are supported :-(")