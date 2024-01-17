print("Test calculator")
print()
noe = input("Name of the exam: ")
print()
nor = int(input("Max score possible: "))
print()
nox = int(input("Your score:  "))
ns = float(nox / nor)
fn = round(ns, 2)
fnpe = round(float(nox / nor,) * 100, 2)
print("Congrats you got", fnpe, "%")
if fnpe >= 90 and fnpe <= 100:
  print("You got an A!")
if fnpe >= 80 and fnpe <= 89:
  print("You got a B!")
if fnpe >= 70 and fnpe <= 79:
  print("You got a C")
if fnpe >= 60 and fnpe <= 69:
  print("You got a D")
if fnpe >= 1 and fnpe <= 59:
  print("You got an F...")
