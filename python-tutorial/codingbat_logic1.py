def cigar_party(cigars, is_weekend):
  if (cigars >= 40 and cigars <= 60) or (cigars >=60 and is_weekend):
   return True
  return False
  
def date_fashion(you, date):
  if (you >= 8 or date >=8):
    if you<=2 or date<=2:
      return 0
    else:
      return 2
  elif you <=2 or date <=2:
    return 0
  else:
    return 1
  
def squirrel_play(temp, is_summer):
  if (temp >=60 and temp <=90) or (temp >=90 and temp <=100 and is_summer):
      return True
  return False

def caught_speeding(speed, is_birthday):
    ticket=0
    if (speed >=61 and speed <=80) and not is_birthday:
      ticket=1
    elif speed >=80 and not is_birthday:
      ticket=2
    elif is_birthday:
      if speed >=86 and speed <87 :
        ticket=1
      elif speed >87:
        ticket=2
    return ticket

def sorta_sum(a, b):
  sum = a+ b
  if sum >= 10 and sum <=19:
    return 20
  else:
    return sum
  
def alarm_clock(day, vacation):
  alarm_status = ["7:00","10:00","off"]
  status=""
  if day >=1 and day <=5:
    if vacation:
      status=alarm_status[1]
    else:
      status=alarm_status[0]
  else:
    if vacation:
      status=alarm_status[2]
    else:
      status=alarm_status[1]
  return status

def love6(a, b):
  if a==6 or b==6 or a+b==6 or abs(a-b)==6:
    return True
  return False

def in1to10(n, outside_mode):
  if not outside_mode:
    if n>=1 and n<=10:
      return True
    else:
      return False
  else:
    if n<=1 or n>=10:
      return True
    else:
      return False
  
