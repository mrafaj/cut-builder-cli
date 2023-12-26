from typing import List, Tuple

def read_cutlist(filename: str) -> List[Tuple[str, str, str]]:
    lines = None
    with open(filename) as f:
        lines = [line.strip("\n").split() for line in f.readlines() if line != "\n"]
    if lines:
        # make into tuple
        lines = [(line[0], line[1], line[2]) for line in lines if len(line) == 3]
        return lines
    else:
        return None