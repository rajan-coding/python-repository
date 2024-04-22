def string_times(str, n):
    return str * n

def front_times(str, n):
    str=str[:3]
    return str * n


def string_bits(str):
    s=[ j for i,j in enumerate(str) if i%2==0]
    return "".join(s)
     

def string_splosion(str):
    s=""
    for i in range(len(str)+1):
     s= s+ str[:i]
    return s

def array_count9(nums):
   return len([i for i in nums if i==9])

def array_front9(nums):
  for i,j in enumerate(nums):
     if j==9 and i<4:
        return True
  return False       

def array123(nums):
  return "".join([str(i) for i in nums]).find("123") >=0