def points(games):
    return sum((1, 3, 0)[(x > y) - (x < y)]
               for g in games
               for x, y in [map(int, g.split(":"))])