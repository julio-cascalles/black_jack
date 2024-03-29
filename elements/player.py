from elements.card import CardList


class Player:
    all_players = []
    SHOW_CARDS: callable = lambda player: print('{}:\n{}'.format(
        player.name, ' '.join( str(card) for card in player.hand )
    ))
    CONTENT = lambda x: next(iter(x), None)

    def __new__(cls, name: str):
        found = cls.CONTENT(p for p in cls.all_players if p.name == name)
        if not found:
            if len(cls.all_players) == 2:
                raise IndexError('There are too many players!')
            found = super().__new__(cls)
            found.name = name
            found.hand = CardList()
            cls.all_players.append(found)
        return found

    def draw(self, deck: list):
        self.hand.append(deck.pop(0))
        self.SHOW_CARDS()

    def score(self) -> int:
        total: int = 0
        for card in self.hand:
            total += card.value(-1 if total < 11 else 0)
        return total

    def opponent(self):
        return Player.CONTENT(p for p in Player.all_players if p != self)
