class A:
    varA= "Class A variable"

class B:
    varB = "Class B is created"

class C(A, B):
    varC = "Class C is created"

c1 = C()
print(c1.varA) 
print(c1.varB) 
print(c1.varC) 
