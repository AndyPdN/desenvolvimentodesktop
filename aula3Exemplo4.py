a = 2
b = 8
c = 3
x1 = 0
x2 = 0 
x3 = 0
x4 = 0
delta = b**2 -4 * a * c
print(delta) 

x1 = (-b + delta) 
x2 = x1 / (2 * a)

x3 = (-b - delta) 
x4 =  x3 / (2 * a)



if delta > 0:
    print("Existe duas raízes distintas X¹ e X²")
elif delta == 0:
    print("X.(b/2a)")

