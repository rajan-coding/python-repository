def hello_name(name):
    return "Hello " + name + "!"

def make_abba(a, b):
 return a + b*2 +a

def make_tags(tag, word):
   return f"<{tag}>{word}</{tag}>"


def make_out_word(out, word):
  return out[:2] + word + out[2:]

def extra_end(str):
 return str[len(str)-2:] * 3


def first_two(str):
  return str[:2]

def first_half(str):
 return str[:len(str)/2]

def without_end(str):
    return str[1:len(str)-1]

def combo_string(a, b):
    if len(a)>len(b):
      return b + a + b
    else:
      return a + b + a