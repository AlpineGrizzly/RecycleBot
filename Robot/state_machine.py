from enum import Enum

#State machine, could have different states which can be read at the beginning of each loop, and could be set by other functions
class State(Enum):
    IDLING = 0
    SEARCHING = 1
    APPROACHING = 2
    COLLECTING = 3
    RETURNING = 4
    DEPOSITING = 5

currentState = State.IDLING
power = True
