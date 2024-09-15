a=float(input("enter the number 1: "));
b=float(input("enter the number 2: "));
c=input("enter the calculator symbol (+,-,*,/,%): ");
if c =="+":
    d=a+b;
    print(round(d,3))
elif c == "-":
    d=a-b;
    print(round(d,3))
elif c == "*":
    d=a*b;
    print(round(d,3))
elif c == "/" :
     d=a/b;
     print(round(d,3))
elif c == "%" :
     d=a%b;
     print(round(d,3))
else :
    print(c,"is not valid in calculation symbol")
     
