def filterFehler (list):
    filterdList = []
    anzahl =0
    for l in list:
        if l ==None:
            continue
        if l >-60 and l < 60:
            filterdList.append(l)
            anzahl += 1

    return filterdList,anzahl

def durchschnitt(list):
    sum = 0
    for l in list:
        if l == None:
            continue
        sum += l
    return sum/len(list)

def main():
    try:
        list = [-123,43,-4,5,None,12,14,15,None,69]

        filtert, anzahl = filterFehler (list)
        print(filtert)
        avarage = durchschnitt(filtert)
        print(avarage)
    except:
       print("Fehler")

if __name__ == "__main__":
    main()