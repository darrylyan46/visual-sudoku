from typing import List

def createEmptyGrid(n: int = 3) -> List[int]:
    if n < 0:
        raise ValueError("Argument must be greater than or equal to 0.")
    return [[None for _ in range(n)] for _ in range(n)]
