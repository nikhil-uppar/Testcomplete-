class Cat():
  def __init__(self,name,color,age):
    Log.Message("Using a constructer here")
    self.name = name
    self.color= color
    self.age= age
    
    
  def cname(self):
    return f"cat name is :{self.name}"
  def update_name(self,new_name):
    self.name=new_name
    
    
def testme():
  mycat = Cat("rocky","black" ,11)
  Log.Message(mycat.name)
  Log.Message(mycat.color)
  Log.Message(mycat.age)
  Log.Message(mycat.cname())
  mycat.update_name("fifi")
  Log.Message(mycat.cname())
  
 