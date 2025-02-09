import numpy as np
import random
import logging
#Thankyou codsoft
logging.basicConfig(level=logging.INFO)

class TicTacToeAI:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.player = 'X'  # for me
        self.ai = 'O'      # AI player player

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def check_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board

    def minimax(self, depth, is_maximizing):
        if self.check_winner(self.ai):
            return 1
        if self.check_winner(self.player):
            return -1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = -np.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.ai
                    score = self.minimax(depth + 1, False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = np.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.player
                    score = self.minimax(depth + 1, True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = -np.inf
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.ai
                score = self.minimax(0, False)
                self.board[i] = ' '
                logging.info(f"AI evaluated move {i+1}, score: {score}")
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def player_move(self):
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if self.board[move] == ' ':
                    self.board[move] = self.player
                    break
                else:
                    print("Invalid move. Try again.")
            except (IndexError, ValueError):
                print("Please enter a valid number between 1 and 9.")

    def play_game(self):
        while True:
            # Human player's move
            self.print_board()
            self.player_move()

            if self.check_winner(self.player):
                self.print_board()
                print("You win!")
                break
            if self.check_draw():
                self.print_board()
                print("It's a draw!")
                break

            # AI's move
            ai_best_move = self.ai_move()
            self.board[ai_best_move] = self.ai
            logging.info(f"AI chooses position {ai_best_move+1}")

            if self.check_winner(self.ai):
                self.print_board()
                print("AI wins!")
                break
            if self.check_draw():
                self.print_board()
                print("It's a draw!")
                break

# Main execution
if __name__ == "__main__":
    game = TicTacToeAI()
    game.play_game()
