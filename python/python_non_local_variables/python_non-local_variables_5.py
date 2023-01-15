name="John" 
def one():    
  def two():    
    name="Doe"    
    def three():
      nonlocal name
      name="Stacks"
      print("Name-THREE: ",name)
    three()
    print("Name-TWO: ",name)	
  two()
  print("Name-ONE: ",name)  
one()  