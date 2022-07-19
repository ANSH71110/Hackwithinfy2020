n=int(input())
i=0
a=[]
b=[]
while i<n:
  l=int(input())
  j=l-1
  x=list(map(int, input().split(' ')))
  lt=[]
  start=0
  end=0
  j=0
  while j<l-1:
    if x[j]<=x[j+1]:
      end=j+1
    else:
      if len(lt)<end-start:
        lt=x[start:end+1]
      start=j+1
    j+=1
  if len(lt)<end-start:
    lt=x[start:end+1]
  j=0
  while j<len(lt):
    print(lt[j],end=" ")
    j+=1
  print()
  i+=1
