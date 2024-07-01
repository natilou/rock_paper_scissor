import random
from src.game.constants import GameOptionsEnum, COMPUTER, USER


class Match:

    def __init__(self, user_action: GameOptionsEnum) -> None:
        self.user_action = user_action
        self.computer_action = ""
        self.winner = None

    def play(self) -> None:
        self._choose_computer_action()
        self._resolve_winner()

    def _choose_computer_action(self) -> None:
        self.computer_action = random.choice(list(GameOptionsEnum))

    def get_computer_action(self) -> GameOptionsEnum:
        return self.computer_action

    def _resolve_winner(self) -> None:
        if self.user_action == self.computer_action:
            return

        winning_combinations = {
            GameOptionsEnum.ROCK: GameOptionsEnum.SCISSORS,
            GameOptionsEnum.PAPER: GameOptionsEnum.ROCK,
            GameOptionsEnum.SCISSORS: GameOptionsEnum.PAPER,
        }
        if winning_combinations[self.user_action] == self.computer_action:
            self.winner = USER
        else:
            self.winner = COMPUTER

    def get_match_winner(self) -> str | None:
        return self.winner
