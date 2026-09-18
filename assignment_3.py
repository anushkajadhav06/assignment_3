a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
def triangle(a,b,c):
  if a*a+b*b==c*c:
    print(" it is right angle triangle")
  else:
    print("it is not a right angle triangle")
triangle(a,b,c)