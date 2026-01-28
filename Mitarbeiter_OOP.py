
class Person:
    def __init__(self, name: str, geschlecht: str):
        if geschlecht not in ("m", "w"):
            raise ValueError("Geschlecht muss 'm' oder 'w' sein")
        self.name = name
        self.geschlecht = geschlecht



class Mitarbeiter(Person):
    def __init__(self, name: str, geschlecht: str, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung
        abteilung.mitarbeiter_hinzufuegen(self)



class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name: str, geschlecht: str, abteilung):
        super().__init__(name, geschlecht, abteilung)
        abteilung.setze_leiter(self)


class Abteilung:
    def __init__(self, name: str):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def mitarbeiter_hinzufuegen(self, mitarbeiter: Mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def setze_leiter(self, leiter: Abteilungsleiter):
        if self.leiter is not None:
            raise ValueError("Diese Abteilung hat bereits einen Abteilungsleiter")
        self.leiter = leiter

    def mitarbeiteranzahl(self):
        return len(self.mitarbeiter)



class Firma:
    def __init__(self, name: str):
        self.name = name
        self.abteilungen = []

    def abteilung_hinzufuegen(self, abteilung: Abteilung):
        self.abteilungen.append(abteilung)

    def alle_mitarbeiter(self):
        return [m for a in self.abteilungen for m in a.mitarbeiter]

    def anzahl_mitarbeiter(self):
        return len(self.alle_mitarbeiter())

    def anzahl_abteilungsleiter(self):
        return sum(1 for a in self.abteilungen if a.leiter is not None)

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        return max(self.abteilungen, key=lambda a: a.mitarbeiteranzahl())

    def geschlechter_prozent(self):
        mitarbeiter = self.alle_mitarbeiter()
        if not mitarbeiter:
            return 0, 0

        frauen = sum(1 for m in mitarbeiter if m.geschlecht == "w")
        maenner = sum(1 for m in mitarbeiter if m.geschlecht == "m")

        gesamt = len(mitarbeiter)
        return (frauen / gesamt * 100, maenner / gesamt * 100)

firma = Firma("Tech AG")


it = Abteilung("IT")
hr = Abteilung("Medien")

firma.abteilung_hinzufuegen(it)
firma.abteilung_hinzufuegen(hr)


Abteilungsleiter("Enes", "m", it)
Mitarbeiter("Tim", "m", it)
Mitarbeiter("Moni", "w", it)

Abteilungsleiter("Duyer", "m", hr)
Mitarbeiter("Eva", "w", hr)


print("Mitarbeiter:", firma.anzahl_mitarbeiter())
print("Abteilungsleiter:", firma.anzahl_abteilungsleiter())
print("Abteilungen:", firma.anzahl_abteilungen())
print("Größte Abteilung:", firma.groesste_abteilung().name)

frauen, maenner = firma.geschlechter_prozent()
print(f"Frauen: {frauen:.1f}%, Männer: {maenner:.1f}%")