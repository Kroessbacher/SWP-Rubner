a = 5
names = {"Tom","Tim","Lutwig"}
b =0

if a < 5:
    print("Nein")

for name in names:
    if name == "Tim":
        pass
    pass
    print(name)

while b < 10:
    if b == 9:
        break
    elif b == 5:
        print("b == 5")

    else:
        print(b)

    b += 1

try:
    print("Try")
    print(a)
except NameError:
    print("NameError")
else:
    print("else!")
finally:
    print("Finally")
    print(4)


