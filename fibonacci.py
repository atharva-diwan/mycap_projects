def fibonac(n):
  if n==1:
    print(0,end=' ')
  elif n==2:

    print(0,end=' ')
    print(1,end=' ')
  else:
    t1=0
    t2=1
    print(str(t1)+' '+str(t2),end=' ')
    for i in range(n-2):
      t3=t1+t2
      print(str(t3),end=' ')
      t1=t2
      t2=t3
print("enter no. of terms (greater than 2) to be generated")
num=int(input())
fibonac(num)