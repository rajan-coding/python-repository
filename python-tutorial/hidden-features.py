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