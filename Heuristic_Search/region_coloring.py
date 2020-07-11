from simpleai.search import CspProblem, backtrack

def constraint_function(names, values):
    """Imposes the  constraint that neighbors should be different."""
    return values[0] != values[1]

if __name__ == "__main__":
    names = (
        'Mark', 'Julia', 'Steve', 'Amanda', 'Brian',
        'Joanne', 'Derek', 'Allan', 'Michelle', 'Kelly'
        )
    
    colors = dict((name, ['red', 'green', 'blue', 'grey']) for name in names)
    constraints = [
        (('Mark', 'Julia'), constraint_function),
        (('Mark', 'Steve'), constraint_function),
        (('Julia', 'Steve'), constraint_function),
        (('Julia', 'Amanda'), constraint_function),
        (('Julia', 'Brian'), constraint_function),
        (('Julia', 'Derek'), constraint_function),
        (('Steve', 'Amanda'), constraint_function),
        (('Steve', 'Allan'), constraint_function),
        (('Steve', 'Michelle'), constraint_function),
        (('Amanda', 'Michelle'), constraint_function),
        (('Amanda', 'Derek'), constraint_function),
        (('Brian', 'Derek'), constraint_function),
        (('Brian', 'Kelly'), constraint_function),
        (('Joanne', 'Michelle'), constraint_function),
        (('Joanne', 'Amanda'), constraint_function),
        (('Joanne', 'Kelly'), constraint_function),
        (('Kelly', 'Derek'), constraint_function)
    ]

    problem = CspProblem(names, colors, constraints)

    output = backtrack(problem)
    print('\nColor mapping:\n')
    for k,v in output.items():
        print(k, '==>', v)