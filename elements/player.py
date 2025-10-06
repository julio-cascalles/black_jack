from elements.card import CardList


IS_EQUAL  = lambda x, y: x == y
NOT_EQUAL = lambda x, y: x != y

class Player:
    all_players = []

    def __new__(cls, name: str):
        found = cls.find(name)
        if not found:
            if len(cls.all_players) == 2:
                raise IndexError('There are too many players!')
            found = super().__new__(cls)
            found.name = name
            found.hand = CardList()
            cls.all_players.append(found)
        return found

    @classmethod
    def find(cls, search: str, compare: callable = IS_EQUAL) -> 'Player':
        for player in cls.all_players:
            if compare(player.name, search):
                return player
        return None

    def draw(self, deck: list):
        self.hand.append(deck.pop(0))
        print('{}:\n{}'.format(
            self.name, ' '.join( str(card) for card in self.hand )
        ))

    def score(self) -> int:
        total: int = 0
        for card in self.hand:
            total += card.value(-1 if total < 11 else 0)
        return total

    def opponent(self):
        return self.find(self.name, NOT_EQUAL)
