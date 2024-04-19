values=[ i for i in range(50,100,5) if i %2 ==0]

print(values)

x=lambda x : x + 10
y=lambda y: y%3==0

print(x(3))
print(x(10))

map_values= map(x,values)
print(list(map_values))

filter_values= filter(y,values)
print(list(filter_values))