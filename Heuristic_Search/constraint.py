from simpleai.search import *

def constraint_unique(variables, values):
    """Constraint that expects all the variables to have different values."""
    return len(values) == len(set(values))

def constraint_bigger(variables, values):
    """
    Constraint thet specifies that one variable should be bigger
    than the other.
    """
    return values[0] > values[1]

def constraint_odd_even(variables, values):
    """
    Constraint that specifies that there should be one odd and one
    even variables in the to variables.
    """
    # if first variable is even, then second should be odd and vice versa
    if values[0] % 2 == 0:
        return values[1] % 2 == 1
    else:
        return values[1] % 2 == 0

if __name__ == "__main__":
    variables = ('John', 'Anna', 'Tom', 'Patricia')
    domains = {
        'John':[1, 2, 3],
        'Anna':[1, 3],
        'Tom':[2, 4],
        'Patricia':[2, 3, 4]
    }

    constraints = [
        (('John', 'Anna', 'Tom'), constraint_unique),
        (('Tom', 'Anna'), constraint_bigger),
        (('John', 'Patricia'), constraint_odd_even)
    ]

    problem = CspProblem(variables, domains, constraints)

    print('\nSolutions:\n\nNormal:', backtrack(problem))
    print('\nMost constrained variable:', backtrack(problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))
    print('\nHighest degree variable:', backtrack(problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE))
    print('\nLeast constraining values:', backtrack(problem, value_heuristic=LEAST_CONSTRAINING_VALUE))
    print('\nMost constraines variable and least constraining value:',
        backtrack(problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, 
                value_heuristic=LEAST_CONSTRAINING_VALUE
            )
    )
    print('\nMost constraines variable and least constraining value:',
        backtrack(problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, 
                value_heuristic=LEAST_CONSTRAINING_VALUE
            )
    )
    print('\nMinimum conflicts:', min_conflicts(problem))