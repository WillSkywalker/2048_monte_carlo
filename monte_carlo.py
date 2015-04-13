"""Algorithm for simulate a 2048 game using Monte-Carlo method."""

import random, _2048

SIMULATE_TIMES = 100000
DIRECTIONS = ('UP', 'DOWN', 'LEFT', 'RIGHT')

def simulate_to_end(game):
    while game.get_state():
        dircts = list(DIRECTIONS)
        for i in xrange(3):
            c = random.choice(dircts)
            if game.move(c):
                break
            dircts.remove(c)


    return game.get_score()

def score_sum(game,direction):
    score = 0
    temp = game.clone()
    temp.move(direction)
    for i in xrange(SIMULATE_TIMES):
        score += simulate_to_end(temp)
    return score

def monte_carlo(game):
    scores = {}
    biggest = 0
    directions = list(DIRECTIONS)
    for d in DIRECTIONS:
        test = game.clone()
        if not test.move(d):
            directions.remove(d)
    for direction in directions:
        temp = game.clone()
        score = score_sum(temp, direction)
        if score > biggest:
            biggest = score
            best = direction
        scores[direction] = score
    print scores
    if len(set(scores)) == 1:
        return False
    else:
        return best

if __name__ == '__main__':
    a_game = _2048.Gameplay()
    print monte_carlo(a_game)