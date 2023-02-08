# Many exceptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
finally:
  print("The 'try except' is finished")
  
# Else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")