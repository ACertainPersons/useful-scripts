t=0
try :
    n = int(input("Insert number here: "))
    if n>0 :
        while n!=1:
            print (n)
            if n%2==1 :
                n= 3*n+1
            else :
                n= n/2
            t+=1
        print ("1.0")
        print ()
        print ("steps taken:")
        print (t)
    else: 
        print("Negative numbers (and 0) not supported yet")
except ValueError:
    print("Only integers are supported :-(")