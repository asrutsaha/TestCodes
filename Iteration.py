A = int(input("Input value for A: "))
X = int(input("Input value for X: "))

for i in range(1,X+1):
   print(A,'x',i,'=',A*i)

for j in range(1,2*X+1):
   print(A+1,'x',j,'=',(A+1)*j)

for k in range(1,3*X+1):
   print(A+2,'x',k,'=',(A+2)*k)
