Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ‎⁨class Nummm:
    
    def checkOddEven(num):       
                if num%2==0: 
                    print("this number "+str(num)+" is even number")
                else:
                    print("this number "+str(num)+" is odd number")
            
    print("Easy Calculator for Integer number")         
    n1=int(input("input the first interger: "))
    try:    
        v = int(n1) 
        checkOddEven(v)
    except ValueError:    
        print("it's not an integer!!!!!!")
    
    
    n2=int(input("input the second num: "))
    try:    
        v2 = int(n2) 
        checkOddEven(v2)
    except ValueError:    
        print("it's not an integer!!!!!!")
   
    s=input("insert + or - or * or /: " )
    if s=="+":
        result=n1+n2
    elif s=='-':
        result=n1-n2    
    elif s=='*':
        result=n1*n2
    elif s=='/':
        result=n1/n2
    print ("result might be "+str(result))
    
SyntaxError: invalid character in identifier
>>> 
>>> 


    def checkOddEven(num):       
                if num%2==0: 
                    print("this number "+str(num)+" is even number")
                else:
                    print("this number "+str(num)+" is odd number")
            
    print("Easy Calculator for Integer number")         
    n1=int(input("input the first interger: "))
    try:    
        v = int(n1) 
        checkOddEven(v)
    except ValueError:    
        print("it's not an integer!!!!!!")
    
    
    n2=int(input("input the second num: "))
    try:    
        v2 = int(n2) 
        checkOddEven(v2)
    except ValueError:    
        print("it's not an integer!!!!!!")
   
    s=input("insert + or - or * or /: " )
    if s=="+":
        result=n1+n2
    elif s=='-':
        result=n1-n2    
    elif s=='*':
        result=n1*n2
    elif s=='/':
        result=n1/n2
    print ("result might be "+str(result))
    
SyntaxError: unexpected indent
>>> class Nummm:
    
    def checkOddEven(num):       
                if num%2==0: 
                    print("this number "+str(num)+" is even number")
                else:
                    print("this number "+str(num)+" is odd number")
            
    print("Easy Calculator for Integer number")         
    n1=int(input("input the first interger: "))
    try:    
        v = int(n1) 
        checkOddEven(v)
    except ValueError:    
        print("it's not an integer!!!!!!")
    
    
    n2=int(input("input the second num: "))
    try:    
        v2 = int(n2) 
        checkOddEven(v2)
    except ValueError:    
        print("it's not an integer!!!!!!")
   
    s=input("insert + or - or * or /: " )
    if s=="+":
        result=n1+n2
    elif s=='-':
        result=n1-n2    
    elif s=='*':
        result=n1*n2
    elif s=='/':
        result=n1/n2
    print ("result might be "+str(result))

    
Easy Calculator for Integer number
input the first interger: 1
this number 1 is odd number
input the second num: 2
this number 2 is even number
insert + or - or * or /: *
result might be 2
>>> 
