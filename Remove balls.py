import math 
i=0
cone=int(input())
cthree=0
count=1
while cone>=3:
  cthree+=1
  cone-=3
  count+=int(math.factorial(cone+cthree)/(math.factorial(cthree)*math.factorial(cone)))
print(count%(10**9 +7))
