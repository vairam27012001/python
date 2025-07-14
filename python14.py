a = int(input())
b = int(input())
c = int(input())

d = (b**2) - (4*a*c)
print("Discriminant =", d)

if d > 0:
    x1 = ((-b) + (d**0.5)) / (2*a)
    x2 = ((-b) - (d**0.5)) / (2*a)
    print("Real and Different Roots: ", round(x1, 2), round(x2, 2))

elif d == 0:
    x1 = (-b) / (2*a)
    print("Real and Equal Roots: ", round(x1, 2))

else:
    real_part = (-b) / (2*a)
    imag_part = ((-d)**0.5) / (2*a)
    print("Imaginary Roots:")
    print(f"{real_part} + {imag_part}i")
    print(f"{real_part} - {imag_part}i")





