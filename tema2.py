#Replacing the code below with regular for loop! 
#unique_grid = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(unique_grid)

x = [1,2,3]
y = [3,1,4]
for a in x:
    for b in y:
          if a != b:
                print (a,b)