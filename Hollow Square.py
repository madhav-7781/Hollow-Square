size = 7
#TopRow
for i in range(size):
    print("* ",end="")
print()

#MiddleRow
for i in range(size-2):
    print("*",end="")
    for j in range(size-2):
        print("  ",end="")
    print(" *")
    
#BottomRow
for i in range(size):
    print("* ",end="")
