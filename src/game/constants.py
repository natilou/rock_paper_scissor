import enum


class GameOptionsEnum(str, enum.Enum):
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"

    def __str__(self):
        return f"{self.value} {OPTIONS_EMOJI[self]}"


class ExtraOptionsEnum(str, enum.Enum):
    EXIT = "Exit"

    def __str__(self) -> str:
        return f"{self.value} {OPTIONS_EMOJI[self]}"


OPTIONS_EMOJI = {
    GameOptionsEnum.ROCK: "🪨",
    GameOptionsEnum.PAPER: "📄",
    GameOptionsEnum.SCISSORS: "✂️",
    ExtraOptionsEnum.EXIT: "❌",
}

USER = "User"
COMPUTER = "Computer"
