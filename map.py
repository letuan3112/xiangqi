from chess.chess import Chess, chesses
from chess import chess
from point.point import Point
import setUp

# setup:
setUp.setChess()
# end setup

def renderMap():
    # print map:
    for i in range(-1, 10, 1):
        for j in range(-1, 9, 1):
            if(i == -1):
                if(j == -1):
                    print(' ', end  = ' ')
                else:
                    print(j, end = ' ')
            elif(j == -1 and i > -1):
                print(i, end = ' ')
            p = Point(j, i)
            for chess in chesses:
                chess.update(p)
        print()
    # end print