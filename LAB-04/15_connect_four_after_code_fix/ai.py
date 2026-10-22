import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(7) if board.grid[0][c] == "."]

        if not legal:
            return None

        # 1. Check whether AI can win immediately
        for col in legal:
            row = board.drop(col, me)

            if board.winner(me):
                board.grid[row][col] = "."
                return col

            board.grid[row][col] = "."

        # 2. Check whether player can win next turn
        # and block that column
        for col in legal:
            row = board.drop(col, opponent)

            if board.winner(opponent):
                board.grid[row][col] = "."
                return col

            board.grid[row][col] = "."

        # 3. Otherwise choose a legal column
        return random.choice(legal)