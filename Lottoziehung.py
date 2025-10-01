import random

def main():
    anzahl_ziehungen = 1000
    haeufigkeiten = {i: 0 for i in range(1, 46)}  # Zähler für jede Zahl von 1 bis 45

    for a in range(anzahl_ziehungen):
        zahlen = list(range(1, 46))
        gezogene_zahlen = lottoziehung(zahlen, 6)[-6:]  # letzten 6 sind die gezogenen
        for zahl in gezogene_zahlen:
            haeufigkeiten[zahl] += 1

    #Ausgabe sortiert nach Zahl
    for zahl in range(1, 46):
        print(f"Zahl {zahl:2}: {haeufigkeiten[zahl]} mal gezogen")


def lottoziehung(zahlen, anzahl):
    for x in range(anzahl):
        zufalls_index = random.randint(0, len(zahlen)-1-x)
        zahlen[len(zahlen)-1 - x], zahlen[zufalls_index] = zahlen[zufalls_index], zahlen[len(zahlen)-1-x]
    return zahlen


if __name__ == "__main__":
    main()