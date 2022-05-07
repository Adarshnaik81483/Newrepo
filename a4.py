#program to find the area of triangle.
A=int(input("Enter the value of A"))
B=int(input("Enter the value of B"))
C=int(input("Enter the value of C"))
S=(A+B+C)/2#calculating semi perimeter.
area_of_triangle=(S*(S-A)*(S-B)*(S-C))**0.5
print(area_of_triangle)
