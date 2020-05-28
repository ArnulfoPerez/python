"""Example of using generators to implement backtracking search."""
def queens(bsize):
    """
    The example below is an implementation of the classic "N queens"
    problem (place N queens on an N x N chessboard so that none are
    threatened by the others.)

    Board representation: Since no two queens can be one the same
    row, the board is represented as a tuple of N length, where
    each element is the column occupied by the queen on that row."""


    def threaten(qarray, newpos):
        """Function to test if a queen is threatened by any previously placed queen."""
        # Now check the diagonals
        dist = len(qarray) # Distance between rows
        for queen in qarray:
            if queen == newpos:
                return True # Same column
            if queen + dist == newpos:
                return True # diagonal
            if queen - dist == newpos:
                return True # diagonal
            dist -= 1
        return False

    def qsearch(qarray=()):
        """search for solutions"""
        for queen in range(0, bsize): # Try each position
            if not threaten(qarray, queen): # If not threatened
                pos = qarray + (queen, ) # Append to the pos array
                if len(pos) >= bsize: # Are we done?
                    yield pos # Yield the answer
                else: # recursively call new generator
                    for pos in qsearch(pos):
                        yield pos

    print("Queens problem for"+str(bsize)+"x"+str(bsize)+"board.")
    for ans in qsearch():
        # Print out the board
        print("+" + "---+" * bsize)
        for queen in ans:
            print("|" + " |" * queen + " Q |" + " |" * (bsize - queen - 1))
        print("+" + "---+" * bsize)
        print()

queens(8)
