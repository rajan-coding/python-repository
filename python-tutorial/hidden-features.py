#anonymous variable

coordinate =[5,10]

large_coordinate=[1,2,3]

list_of_pairs=[["A","B"],["C","D"],["E","F"]]

for _ in range(10):
    print("Hello World")

x , _ =coordinate

x, _ , z=large_coordinate

second_elements=[ y for  _ , y in list_of_pairs]

print(second_elements)

# while else, for else


items =["a","b","c","d","e","f"]
i=0

while i < len(items):
    item = items[i]

    if items =="z":
        print("found it")
        break
    
    i +=1
else:
    print("not found")

for item in items:
    
    if items =="z":
        print("found it")
        break
    
    i +=1
else:
    print("not found")

# argument unpacking


def numbers(a,b,c,d):
    print(a,b,c,d)

list=["a","b","c","d"]

numbers(*list)

values ={
    "key":"5",
    "target":10
}

def parse_value(key,target):
    print(key,target)

parse_value(**values)