#fraction has
#numerator - int
#denominator - int

#fractions can-dos
#add itself (fraction), output = fraction
#multiply (fraction), output = fraction
#recipricol () output = fraction
#simplify(), output = fraction

class Fraction:

  def __init__(self, top, bottom):
      self.top = top
      self.bottom = bottom

  def fracAdd(self, operand):
      commonD = self.bottom * operand.bottom
      newtop = self.top * operand.bottom
      newtop2 = operand.top * self.bottom
      finalnum = newtop + newtop2
      answer = Fraction(finalnum,commonD)
      return answer


  def mltply(self, operand):
      answer = self.top


  def recip(self):
      nbottom = self.top
      ntop = self.bottom
      print((str(ntop)) + "/" + (str(nbottom)))

  def __str__(self):
     return str(self.top) + "/" + str(self.bottom)


bob = Fraction(2,4)
f2 = Fraction(3,4)
print(bob.fracAdd(f2))
bob.mltply()
bob.recip()
