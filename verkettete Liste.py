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
        self.count =0

    def getFirstElem(self):
        return self.startElem

    def addLast(self, obj):
        newElem = ListElement(obj)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)
        self.count +=1

    def getLastElem(self):
        le = self.startElem
        while le.getNextElem() is not None:
            le = le.getNextElem()
        return le

    def insertAfter(self, prevItem, newItem):
        pointerElem = self.startElem.getNextElem()
        while pointerElem is not None and pointerElem.getObj() is not prevItem:
            pointerElem = pointerElem.getNextElem()

        newElem = ListElement(newItem)
        nextElem = pointerElem.getNextElem()
        pointerElem.setNextElem(newElem)
        newElem.setNextElem(nextElem)
        self.count +=1

    def delete(self, obj):
        le = self.startElem
        while le.getNextElem() is not None and le.getObj() is not obj:
            if le.getNextElem().getObj() is obj:
                if le.getNextElem().getNextElem() is not None:
                    le.setNextElem(le.getNextElem().getNextElem())
                else:
                    le.setNextElem(None)
                self.count -=1
                break
            le = le.getNextElem()

    def bool_find(self, obj):
        le = self.startElem
        while le is not None:
            if le.getObj() is obj:
                return True
            le = le.getNextElem()
        return False

    def find(self, obj):
        le = self.startElem
        while le is not None:
            if le.getObj() is obj:
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

def main():
    list = EinfachVerketteteListe()
    list.addLast("1")
    list.addLast("2")
    list.addLast("3")
    list.addLast("4")
    list.addLast("5")
    list.insertAfter("2","neu")
    list.writeList()
    list.delete("3")
    list.writeList()

    print("count of elements:", list.getLength())
    print("erstes Element: "+ list.getFirstElem().getObj())
    print("ist '3' enthalten?" + str(list.bool_find("3")))
    print("ist '5' enthalten?" + str(list.bool_find("5")))
    print("ist '5' enthalten?" + list.find("5").getObj())
    print("letztes Element: " + list.getLastElem().getObj())

if __name__ == "__main__":
    try:
        main()
    except:
        print("fehler")