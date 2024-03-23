#empty lists
all_calculations = []
Max_Cals = 5

get_item = ""
while get_item != "xxx":
  get_item = input("Enter an item: ")
  if get_item != "xxx":
    all_calculations.append(get_item)
  
#test Line
all_calculations.reverse()
# Show all items in the list
print("All items in the list:")
for item in all_calculations:
  print(item)

# Show only the first Max_Cals items if they exist
print("\nFirst", Max_Cals, "items:")
for i in range(min(Max_Cals, len(all_calculations))):
  print(all_calculations[i])