import pytest
from src.game.constants import USER, COMPUTER
from src.game.match import Match


class TestMatch:

    @pytest.mark.parametrize(
        "user_choice,computer_choice,expected",
        [
            ("Rock", "Scissors", USER),
            ("Rock", "Paper", COMPUTER),
            ("Paper", "Scissors", COMPUTER),
            ("Paper", "Rock", USER),
            ("Scissors", "Rock", COMPUTER),
            ("Scissors", "Paper", USER),
            ("Rock", "Rock", None),
            ("Paper", "Paper", None),
            ("Scissors", "Scissors", None),
        ]
    )
    def test_resolve_winner(self, user_choice, computer_choice, expected):
        match = Match(user_action=user_choice)
        match.computer_action = computer_choice
        match._resolve_winner()
        assert match.get_match_winner() == expected
