import random

# ================================
# Poker Simulator
# ================================


# --- Eine Hand ziehen ---
def draw_hand(deck):
    """Zieht zufällig 5 verschiedene Karten."""
    return random.sample(deck, 5)


# --- Zähle wie oft jeder Wert vorkommt ---
def count_ranks(hand):
    """Erstellt ein Dictionary mit der Anzahl jedes Kartenwerts."""
    counts = {}
    for card in hand:
        rank = card[:-1]  # alles außer letztes Zeichen (die Farbe)
        #ternäre Operator
        counts[rank] = counts[rank] + 1 if rank in counts else 1
    return counts


# --- Kombination erkennen ---
def evaluate_hand(hand):
    """Erkennt einfache Pokerkombinationen."""
    rank_counts = count_ranks(hand)
    values = list(rank_counts.values())

    # Farben prüfen
    suits_in_hand = []
    for card in hand:
        suits_in_hand.append(card[-1])
    is_flush = len(set(suits_in_hand)) == 1

    # Ränge in Zahlen für Straße
    rank_values = []
    rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for card in hand:
        rank = card[:-1]
        rank_values.append(rank_order.index(rank))
    rank_values.sort()

    is_straight = True
    for i in range(1, len(rank_values)):
        if rank_values[i] - rank_values[i - 1] != 1:
            is_straight = False
            break

    # Kombination bestimmen (einfacher Aufbau)
    if is_straight and is_flush:
        return "Straight Flush"
    elif 4 in values:
        return "Four of a Kind"
    elif 3 in values and 2 in values:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif 3 in values:
        return "Three of a Kind"
    elif values.count(2) == 2:
        return "Two Pair"
    elif 2 in values:
        return "One Pair"
    else:
        return "High Card"


# --- Simulation ---
def simulate(games, deck):
    """Simuliert mehrere Pokerhände und zählt die Kombinationen."""
    results = {}  # Dictionary für Ergebnisse
    for i in range(games):
        hand = draw_hand(deck)
        combo = evaluate_hand(hand)
        if combo in results:
            results[combo] = results[combo] + 1
        else:
            results[combo] = 1
    return results


# --- Ausgabe als Tabelle ---
def print_results(results, total):
    print("Poker Simulation über", total, "Spiele")
    print("------------------------------------")
    for combo in results:
        percent = results[combo] / total * 100
        print(combo, ":", results[combo], "(", round(percent, 4), "% )")
    print("------------------------------------")


def main():
    try:
        games = int(input("Anzahl an Durchläufe: "))
        suits = ['♠', '♥', '♦', '♣']  # vier Farben
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # 13 Werte

        deck = [rank + suit for suit in suits for rank in ranks]

        results = simulate(games, deck)
        print_results(results, games)

    except:
        print("es gibt einen Fehler")
        return



if __name__ == "__main__":
    main()

