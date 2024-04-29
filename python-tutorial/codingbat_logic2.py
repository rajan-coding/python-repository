def lone_sum(a, b, c):
    s = set()
    s.add(a)
    s.add(b)
    s.add(c)

    sum=0

    for i in s :
        sum +=i
    
    return sum


def lucky_sum(a, b, c):
  
  sum =0

  lst=[]
  lst.append(a)
  lst.append(b)
  lst.append(c)

  for i in lst:
     if i == 13 :
        break
     else:
        sum +=i

  return sum


def no_teen_sum(a, b, c):
   sum =0
   lst=[]
   lst.append(a)
   lst.append(b)
   lst.append(c)

   for i in lst:
     if (i !=15 and i!=16 and  i >=13 and i <= 19):
        continue
     else:
        sum +=i

   return sum


   


