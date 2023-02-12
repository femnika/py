def rgb2hex(r, g, b):
    return "#" + f"{r:02x}" + f"{g:02x}" + f"{b:02x}"


r = int(input("Enter Red(0-255): "))
while not 0 <= r <= 255:
    r = int(input("Enter Red(0-255): "))

g = int(input("Enter Green(0-255): "))
while not 0 <= g <= 255:
    g = int(input("Enter Green(0-255): "))

b = int(input("Enter Blue(0-255): "))
while not 0 <= b <= 255:
    b = int(input("Enter Blue(0-255): "))


print(rgb2hex(r, g, b))