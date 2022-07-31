class Rectangle:
  def __init__(self,wid,hei):
    self.width=wid
    self.height=hei

  def set_width(self,wid):
    self.width=wid
  def set_height(self,hei):
    self.height=hei
  def get_area(self):
    return(self.width*self.height)
  def get_perimeter(self):
    return(2*(self.width+self.height))
  def get_diagonal(self):
    return(((self.width ** 2 + self.height ** 2) ** .5))
  def get_picture(self):
    if (self.height>50 or self.width>50):
      return("Too big for picture.")
    picture="*"*self.width+"\n"
    picture*=self.height
    return picture
  def __str__(self):
    return("Rectangle(width="+str(self.width)+", height="+str(self.height)+")")
  def get_amount_inside(self,obj):
    return (self.get_area()// obj.get_area())

    
    
    
  



class Square(Rectangle):
  def __init__(self,sq):
    super().__init__(sq,sq)
  def set_side(self,sq):
    self.width=sq
    self.height=sq
  def __str__(self):
    return("Square(side="+str(self.width)+")")
