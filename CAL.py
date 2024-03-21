def to_celsius(to_convert):
  answer = (to_convert - 32) * 5 / 9
  return round(answer)
def to_fahrenheit(to_convert):
  answer = (to_convert * 9 / 5) + 32
  return round(answer)

to_c_test =[0, 100, 40, -273]
to_f_test =[0, 100, -459]

for item in to_c_test:
  print("{} C is {} F".format(item, to_fahrenheit(item)))
print()
for item in to_f_test:
  print("{} F is {} C".format(item, to_celsius(item)))