from elements.card import Card
from random import shuffle
from itertools import cycle
from elements.player import Player


class Game:
    def __init__(self, rounds:int=6):
        self.deck = [
            Card(name, color) for name in Card.TYPES
            for color in Card.COLORS
        ]
        shuffle(self.deck)
        self.players = cycle([Player('Alice'), Player('Bob')])
        self.winner = None
        self.rounds = rounds
    
    def turn(self) -> str:
        player = next(self.players)
        player.draw(self.deck)
        self.ranking = {p.score(): p for p in (player, player.opponent())}
        score = list(self.ranking)[0]
        if score > 21:
            self.winner = player.opponent()
            return 'Opponent was over 21.'
        elif score == 21:
            self.winner = player
            return 'Achieved the objective!'
        self.rounds -= 1
        if self.rounds == 0:            
            self.winner = self.ranking[max(self.ranking)]
            return 'No more rounds.'
        return ''
