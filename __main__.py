from elements.game import Game


game = Game()
status = 'Starting...'
while not game.winner:
    if game.rounds % 2 == 0:
        print('-'*30)
    status = game.turn()
print('='*30)
print('Winner: {} - {}'.format(
    game.winner.name, status
))
print('-'*30)
print('RANKING:')
print(
    '\n'.join(
        '\t{} = {}'.format(
            player.name, points
        )
        for points, player in game.ranking.items()
    )
)
print('='*30)
