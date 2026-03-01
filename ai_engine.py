import chess
import chess.engine

def main():
    # Path to your Stockfish executable
    stockfish_path = "path/to/your/stockfish"

    # Set up the chess board
    board = chess.Board()

    # Initialize the Stockfish engine
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        while not board.is_game_over():
            print(board)
            move = engine.play(board, chess.engine.Limit(time=2.0))
            board.push(move.move)

        print("Game over. Result: ", board.result())

if __name__ == "__main__":
    main()