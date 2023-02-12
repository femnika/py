def hex2rgb(hex):
    return f"Red: {int(hex[0:2], 16)}, Green: {int(hex[2:4], 16)}, Blue: {int(hex[4:], 16)}"


hex = input("Enter Hex(Eg. #000000 or 000000): ")

while not ((hex[0] == "#" and len(hex) == 7) or (hex[0] != "#" and len(hex) == 6)):
    hex = input("Enter Hex(Eg. #000000 or 000000): ")

if hex[0] == "#":
    hex = hex[1:]

print(hex2rgb(hex))