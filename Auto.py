class Auto:
    def __init__(self, ps):
        self.ps = ps


    def __len__(self):
        return self.ps


    def __add__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Addition nur mit Auto-Objekten möglich")
        return self.ps + other.ps


    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Subtraktion nur mit Auto-Objekten möglich")
        return self.ps - other.ps


    def __mul__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Multiplikation nur mit Auto-Objekten möglich")
        return self.ps * other.ps


    def __eq__(self, other):
        if not isinstance(other, Auto):
            return False
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Vergleich nur mit Auto-Objekten möglich")
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Vergleich nur mit Auto-Objekten möglich")
        return self.ps > other.ps

    def __str__(self):
        return f"Auto mit {self.ps} PS"

a1 = Auto(50)
a2 = Auto(60)


print(len(a1))


print(a1 + a2)


print(a2 - a1)


print(a1 * a2)


print(a1 == a2)
print(a1 < a2)
print(a2 > a1)


