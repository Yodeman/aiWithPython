from simpleai.search import astar, SearchProblem

class PuzzleSolver(SearchProblem):

    def actions(self, cur_state):
        """
        Method to get list of the possible numbers that can be
        moved into the empty space.
        """
        rows = string_to_list(cur_state)
        empty_row, empty_col = get_location(rows, 'e')
        actions = []
        if empty_row > 0:
            actions.append(rows[empty_row - 1][empty_col])
        if empty_row < 2:
            actions.append(rows[empty_row + 1][empty_col])
        if empty_col > 0:
            actions.append(rows[empty_row][empty_col - 1])
        if empty_col < 2:
            actions.append(rows[empty_row][empty_col + 1])
        return actions
    
    def result(self, state, action):
        """
        Return the resulting state after moving a piece to the empty space
        """
        rows = string_to_list(state)
        empty_row, empty_col = get_location(rows, 'e')
        new_row, new_col = get_location(rows, action)
        rows[empty_row][empty_col], rows[new_row][new_col] = \
            rows[new_row][new_col], rows[empty_row][empty_col]
        
        return list_to_string(rows)

    def is_goal(self, state):
        """Returns true if the state is the goal."""
        return state == GOAL

    def heuristic(self, state):
        """
        Returns an estimate of the distance from a state to the
        goal using the manhanttan distance.
        """
        rows = string_to_list(state)
        distance = 0
        for number in '12345678e':
            new_row, new_col = get_location(rows, number)
            new_row_goal, new_col_goal = goal_positions[number]
            distance += abs(new_row-new_row_goal)+abs(new_col-new_col_goal)
        return distance

def list_to_string(input_list):
    return '\n'.join('-'.join(x) for x in input_list)

def string_to_list(input_string):
    return [x.split('-') for x in input_string.split('\n')]

def get_location(rows, input_element):
    """find the 2D location of the input element."""
    for i,row in enumerate(rows):
        for j, item in enumerate(row):
            if item.strip() == input_element:
                return i,j

GOAL =  """1-2-3
4-5-6
7-8-e"""

# Starting point
INITIAL =   """1-e-2
6-3-4
7-5-8"""

goal_positions = {}
goal_rows = string_to_list(GOAL)
for number in '12345678e':
    goal_positions[number] = get_location(goal_rows, number)

result = astar(PuzzleSolver(INITIAL))
#Print the result
for i,(action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path())-1:
        print('After movin', action, 'into the empty space. Goal achieved!')
    else:
        print('After moving', action, 'into the empty space')
    print(state)
