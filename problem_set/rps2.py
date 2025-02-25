import random

class Player():
    def make_move(self):
        while True:
            print(f"What is your move? Please choose r, p, or s")
            move = input().lower()
            if move in ['r','p','s']:
                break
            print(f"Not a valid response")
            
        match move:
            case 'r':
                return Move('Rock')
            case 'p':
                return Move('Paper')
            case 's':
                return Move('Scissors')

class Computer():
    def make_move(self):
        return [Move('Rock'),Move('Paper'),Move('Scissors')][random.randint(0,2)]

class Move():
    def __init__(self, move):
        self.move = move

    def __gt__(self, other):
        if self.move == other.move:
            return False
        elif self.move == 'Rock' and other.move == 'Paper':
            return True
        elif self.move == 'Paper' and other.move == 'Scissors':
            return True
        elif self.move == 'Scissors' and other.move == 'Rock':
            return True
        else:
            return False
    
    def __eq__(self, other):
        return self.move == other.move

class RPSGame():
    def __init__(self):
        pass

    p1 = Player()
    p2 = Computer()
    
    p1__move = p1.make_move()
    p2__move = p2.make_move() 

    print ( p1__move.move )
    print ( p2__move.move )
    print ( p1__move < p2__move )

