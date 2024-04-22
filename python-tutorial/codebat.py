def sleep_in(weekday, vacation):
    sleep_in = True
    if weekday and not vacation:
        sleep_in=False
    return sleep_in


def monkey_trouble(a_smile, b_smile):
    in_trouble=True
    if (a_smile and not b_smile) or (not a_smile and b_smile):
        in_trouble=False
    return in_trouble
  

def sum_double(a, b):
    sum=a+b
    if a==b:
      sum *=2
    return sum

def diff21(n):
    diff=21-n
    if n > 21:
        diff*=2
    return abs(diff)

def parrot_trouble(talking, hour):
  trouble=False
  if talking and (hour < 7 or hour > 20):
      trouble=True
  return trouble

def makes10(a, b):
    return (a+b==10) or (a==10 or b==10)

def near_hundred(n):
    return abs(100-n)<=10 or abs(200-n)<=10


def pos_neg(a, b, negative):
    negative_number=False
    if (negative and (a<0 and b <0)):
        negative_number=True
    elif (not negative_number and(a<0 and b<0)):
        negative_number=False
    elif(not negative and (a<0 or b <0)):
        negative_number=True
    return negative_number

def not_string(str):
    if not str.startswith("not"):
      return "not" + str
    else:
      return str
    
def missing_char(str, n):
    s=list(str)
    s[n]=""
    return "".join(s)

def front_back(str):
    if len(str)==1 or len(str)==0:
     return str
    s=list(str)
    temp=s[0]
    s[0]=s[len(s)-1]
    s[len(s)-1]=temp
    return "".join(s)

def front3(str):
    if len(str) <=3:
        s=str*3
        return s
    else:
        s=list(str)
        s=s[:3]
        s="".join(s) * 3
        return s
    

print(front3("Java"))