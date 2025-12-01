N =5
SS=0
for i in range(1,N,2):
    i = int(input("please input a int :"))
    SS += i
    print("i=",i)
print("sum =",SS)
print("ave =",SS/(N-1))
