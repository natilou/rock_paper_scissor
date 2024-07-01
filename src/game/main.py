import questionary
from src.game.constants import GameOptionsEnum, ExtraOptionsEnum, USER, COMPUTER
from src.game.match import Match


class Game:

    def __init__(self) -> None:
        self.scores = {
            USER: 0,
            COMPUTER: 0,
        }
        self.round_number = 0
        self.is_playing = True

    def start_game(self) -> None:
        while self.is_playing:
            self._play_match()
            questionary.print(f"Scores: {self.scores}")

        final_winner = self._get_final_winner()
        questionary.print(f"Total matches: {self.round_number}")
        if final_winner:
            questionary.print(f"Final scores: {self.scores}")
            questionary.print(f"{final_winner} wins the game! 🏆")
        else:
            questionary.print("It's a tie!")
        questionary.print("Thanks for playing!")

    def _play_match(self) -> None:
        user_action = questionary.select(
            "Choose an action",
            choices=list(GameOptionsEnum) + list(ExtraOptionsEnum),
        ).ask()
        if not user_action or user_action == ExtraOptionsEnum.EXIT.value:
            self.is_playing = False
            return

        match = Match(user_action=user_action)
        match.play()
        computer_action = match.get_computer_action()
        questionary.print(f"{COMPUTER} chose {computer_action}")
        match_winner = match.get_match_winner()
        if not match_winner:
            questionary.print("It's a tie!")
        else:
            questionary.print(f"{match_winner} wins!")
            self.scores[match_winner] += 1
        self.round_number += 1

    def _get_final_winner(self) -> str | None:
        if self.scores[USER] > self.scores[COMPUTER]:
            return USER
        elif self.scores[USER] < self.scores[COMPUTER]:
            return COMPUTER
        return None


if __name__ == "__main__":
    questionary.print("Welcome to Rock🪨, Paper 📄, Scissors ✂️ game!")
    game = Game()
    game.start_game()
