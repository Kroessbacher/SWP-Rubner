"""
This Task should show how a LinkedList works and what functions it can have.
It includes these functions:
    add an object to the end
    add an object after an object of your choice
    delete an object without knowing the location
    finding an object in the list
    finding out if the object is in the list (bool)
    get the first or last object
    printing out the whole list
    getting the count of objects
"""
import random

class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None

    def setNextElem(self, nextElem):
        self.nextElem = nextElem

    def getNextElem(self):
        return self.nextElem

    def getObj(self):
        return self.obj


class EinfachVerketteteListe:
    def __init__(self):
        self.startElem = ListElement("Kopf")
        self.count = 0

    # --- Vorhandene Methoden ---
    def getFirstElem(self):
        return self.startElem

    def addLast(self, obj):
        newElem = ListElement(obj)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)
        self.count += 1

    def getLastElem(self):
        le = self.startElem
        while le.getNextElem() is not None:
            le = le.getNextElem()
        return le

    def insertAfter(self, prevItem, newItem):
        # Nutze '==' für Wertvergleiche bei Strings/Zahlen
        pointerElem = self.startElem.getNextElem()
        while pointerElem is not None and pointerElem.getObj() != prevItem:
            pointerElem = pointerElem.getNextElem()

        if pointerElem:
            newElem = ListElement(newItem)
            nextElem = pointerElem.getNextElem()
            pointerElem.setNextElem(newElem)
            newElem.setNextElem(nextElem)
            self.count += 1

    def delete(self, obj):
        le = self.startElem
        while le.getNextElem() is not None:
            if le.getNextElem().getObj() == obj:
                le.setNextElem(le.getNextElem().getNextElem())
                self.count -= 1
                return  # Beenden nach dem Löschen
            le = le.getNextElem()

    def bool_find(self, obj):
        le = self.startElem
        while le is not None:
            if le.getObj() == obj:
                return True
            le = le.getNextElem()
        return False

    def find(self, obj):
        le = self.startElem
        while le is not None:
            if le.getObj() == obj:
                return le
            le = le.getNextElem()
        return None

    def writeList(self):
        le = self.startElem
        while le is not None:
            print(le.getObj())
            le = le.getNextElem()

    def getLength(self):
        return self.count

    # --- NEU: Iterator Protokoll ---
    def __iter__(self):
        # Wir starten beim ersten Element NACH dem Kopf
        self._currentIter = self.startElem.getNextElem()
        return self

    def __next__(self):
        if self._currentIter is not None:
            data = self._currentIter.getObj()
            self._currentIter = self._currentIter.getNextElem()
            return data
        else:
            raise StopIteration


def main():
    my_list = EinfachVerketteteListe()

    # 1. Befüllen mit Zufallszahlen (Ganzzahl-werte)
    print("Befülle Liste mit 5 Zufallszahlen:")
    for _ in range(5):
        zufallszahl = random.randint(1, 100)
        my_list.addLast(zufallszahl)

    # 2. Test der restlichen Funktionen
    my_list.addLast("TestObjekt")
    my_list.insertAfter("TestObjekt", "Nachfolger")

    print("\nAktuelle Liste:")
    my_list.writeList()

    # 3. Test Iterator
    print("\nAusgabe über Iterator-Schleife:")
    for item in my_list:
        print(f"Iterator-Item: {item}")

    print("\nStats & Suche:")
    print(f"Anzahl Elemente: {my_list.getLength()}")
    print(f"Erstes Element (Kopf): {my_list.getFirstElem().getObj()}")
    print(f"Ist 'TestObjekt' enthalten? {my_list.bool_find('TestObjekt')}")

    my_list.delete("TestObjekt")
    print(f"Nach Löschen - Ist 'TestObjekt' enthalten? {my_list.bool_find('TestObjekt')}")
    print(f"Letztes Element: {my_list.getLastElem().getObj()}")


if __name__ == "__main__":
    main()