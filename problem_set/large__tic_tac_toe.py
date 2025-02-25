class Player:
    def choose_square(self, board):
        while True:
            choice = input("Please input a which square you would like to select: ")
            if choice not in board.open_squares():
                print ("Not a valid option. Please select an available square")
            else:
                square = board.squares[choice]
                square.mark = "X"
                break

class Computer:
    def choose_square(self, board):
        import random
        choice = random.choice(board.open_squares())
        square = board.squares[choice]
        square.mark = "O"

class Board:
    def __init__(self):
        self.squares = {str(key) : Square() for key in range(1,10)}
    
    def display(self):
        print (f"       |       |       ")
        print (f"   {self.squares['1']}   |   {self.squares['2']}   |   {self.squares['3']}   ")
        print (f"       |       |       ")
        print (f"-----------------------")
        print (f"       |       |       ")
        print (f"   {self.squares['4']}   |   {self.squares['5']}   |   {self.squares['6']}   ")
        print (f"       |       |       ")
        print (f"-----------------------")
        print (f"       |       |       ")
        print (f"   {self.squares['7']}   |   {self.squares['8']}   |   {self.squares['9']}   ")
        print (f"       |       |       ")

    def open_squares(self):
        return [key for (key,value) in self.squares.items() if value.mark == " "]

    def is_full(self):
        return len(self.open_squares()) == 0

    def winner(self):
        winning_combos = [[1,2,3], [4,5,6], [7,8,9],[1,4,7], [2,5,8], [3,6,9],[1,5,9],[3,5,7]]
        player_marks = [int(key) for (key,value) in self.squares.items() if value.mark == "X"]
        computer_marks = [int(key) for (key,value) in self.squares.items() if value.mark == "O"]
        for combo in winning_combos:
            if set(combo).issubset(set(player_marks)):
                return 'Player'
            if set(combo).issubset(set(computer_marks)):
                return 'Computer'
        return None
    
    def is_won(self):
        return bool(self.winner())

class Square:
    def __init__(self):
        self._mark = " "
    
    def __str__(self):
        return self._mark
    
    @property
    def mark(self):
        return self._mark
    
    @mark.setter
    def mark(self, mark):
        self._mark = mark

class TTTGame:
    def welcome_message(self):
        print("Welcome to Tic Tac Toe: ")

    def exit_message(self):
        print("Thanks for Playing! ")

    def play(self):
        self.welcome_message()
        self.board, self.player, self.computer = Board(), Player(), Computer()
        while True:
            self.board.display()
            if (not self.board.is_won()) and (not self.board.is_full()):
                self.player.choose_square(self.board)
            else:
                break
            if (not self.board.is_won()) and (not self.board.is_full()):
                self.computer.choose_square(self.board)
            else:
                break
        self.board.display()
        if self.board.winner() == 'Player':
            print ("Congratulations, you win!")
        elif self.board.winner() == 'Computer':
            print ("Sorry, you lost :/")
        else:
            print ("We Tied")
        
        self.exit_message()

game = TTTGame()

game.play()


#### NEXT STEPS: FIX IS_WON / WINNER; FIX END OF GAME FOR INDEX ERROR; MAKE COMPUTER SMARTER