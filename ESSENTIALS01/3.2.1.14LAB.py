blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
current_floor_requirement = 1
height = 0
while blocks >= current_floor_requirement:
    blocks -= current_floor_requirement
    height += 1
    current_floor_requirement += 1
print("The height of the pyramid:", height)
#	
