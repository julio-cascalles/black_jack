from colorama import init, Fore, Back, Style

init(autoreset=True)


class Card:
    TYPES = {'A': [1, 11]} | {c: [10] for c in 'JQK'
    } | {
        str(i): [i] for i in range(2, 11)
    }
    COLORS = {
        'clubs': Back.WHITE+Fore.BLACK + "{}♣",
        'hearts': Fore.RED + "{}♥",
        'spades': Back.WHITE+Fore.BLACK + "{}♠",
        'diamonds': Fore.RED + "{}♦",
    }

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = self.COLORS[color] + Style.RESET_ALL

    def __str__(self) -> str:
        return self.color.format(self.name)

    def value(self, index: int=0) -> int:
        return self.TYPES[self.name][index]


class CardList(list):
    def append(self, card: Card):
        if card.name != 'A':
            return self.insert(0, card)
        super().append(card)
