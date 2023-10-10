"""
CS150 Towers of Hanoi example
"""

def move_disk(label, pole1, pole2):
    """
    Move disk 'label' from pole1 to pole2
    Args:
        label: label of disk to move
        pole1: label of pole to move disk from
        pole2: label of pole to move disk to
    Returns:
        None
    """
    print("Move disk "+str(label)+" from " + pole1 + " to " + pole2)

def hanoi(n, start_pole, final_pole, spare_pole):
    """
    Move disks from `from_pole` to `to_pole`
    Args:
        n: number of disks in the puzzle
        start_pole: label of start pole
        final_pole: label of destination pole
        spare_pole: label of extra pole
    Returns:
        None
    """
    if n == 1:
        move_disk(n, start_pole, final_pole)
    else:
        hanoi(n-1, start_pole, spare_pole, final_pole)
        move_disk(n, start_pole, final_pole)
        hanoi(n-1, spare_pole, final_pole, start_pole)
        
# hanoi(4, 'A', 'B', 'C')
