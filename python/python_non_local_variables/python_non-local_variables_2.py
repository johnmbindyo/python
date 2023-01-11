def printname():
  name="John"   
  def innerprintname():
    #nonlocal name
    name="Doe"
    print("Name-Inner: ",name)	
  innerprintname()
  print("Name-Outer: ",name)  
printname()  