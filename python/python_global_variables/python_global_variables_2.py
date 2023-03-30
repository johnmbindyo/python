#initial value
name="John"
print(name)

def printname():
  #name is changed to have value "Doe"
  name="Doe"
  #When we print below,we are accessing value "Doe"
  print("Name: ",name)  
printname() 
#Here we are accessing the old value "John" 
print(name)