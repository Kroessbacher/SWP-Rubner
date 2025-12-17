import sys


def filter_errors(list):
    filteredList = [l for l in list if l !=None and -60<l<60 ]
    errors = len(list) - len(filteredList)
    return filteredList,errors

def avarage(list):
    if len(list) == 0:
        return 0
    return sum(list)/len(list)

def main():
    list = [-123,43,-4,5,None,12,14,15,None,69]
    filteredList,errors = filter_errors(list)
    print(filteredList)
    print(errors)

    avg = avarage(filteredList)
    print(avg)

if __name__ == "__main__":
    try:
        main()
    except:
        print("Fehler")
        sys.exit(1)