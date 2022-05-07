#program to solve the quadratic equation.
import cmath
A=int(input("enter the value of A:"))
B=int(input("enter the value of B:"))
C=int(input("enter the value of C:"))
d=(B**2)-(4*A*C)
soln1=(-B-cmath.sqrt(d))/(2*A)
soln2=(-B+cmath.sqrt(d))/(2*A)
print("the solutions are{0} and {1}".format(soln1,soln2))
