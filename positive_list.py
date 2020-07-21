list1=list(map(int,input().split()))
def print_pos(l):
  #arguments: l= input list
  for i in range(len(l)):
    if l[i]>0:
      print(l[i],end=' ')
print_pos(list1)