import unittest
from unittest.mock import patch
from poker import count_ranks, evaluate_hand, simulate  # <-- Dateiname anpassen


class TestPokerFunctions(unittest.TestCase):

    def test_count_ranks(self):
        """Testet, ob die Kartenwerte korrekt gezählt werden."""
        hand = ["A♠", "A♥", "10♦", "5♣", "5♠"]
        result = count_ranks(hand)
        expected = {"A": 2, "10": 1, "5": 2}
        self.assertEqual(result, expected)

    def test_evaluate_one_pair(self):
        """Testet eine einfache 'One Pair'-Hand."""
        hand = ["K♠", "K♦", "3♥", "7♣", "9♠"]
        result = evaluate_hand(hand)
        self.assertEqual(result, "One Pair")

    def test_evaluate_straight_flush(self):
        """Testet eine Straight Flush Hand."""
        hand = ["6♣", "7♣", "8♣", "9♣", "10♣"]
        result = evaluate_hand(hand)
        self.assertEqual(result, "Straight Flush")

    @patch("poker.draw_hand")
    def test_simulate(self, mock_draw):
        """Simuliert deterministisch, ob die Ergebnisse korrekt gezählt werden."""
        # Wir tun so, als würde jede Runde 'One Pair' gezogen
        mock_draw.return_value = ["K♠", "K♦", "3♥", "7♣", "9♠"]

        deck = []
        games = 5
        result = simulate(games, deck)

        self.assertEqual(result, {"One Pair": 5})


if __name__ == "__main__":
    unittest.main()