from kanren import *
from kanren.core import lall

people = var()

# Define the rules
rules = lall(
        # There are 4 people
        (eq, (var(), var(), var(), var()), people),

        # Steve's car is blue
        (membero, ('Steve', var(), 'blue', var()), people),

        # Person who has a cat lives in Canada
        (membero, (var(), 'cat', var(), 'Canada'), people),

        # Matthew lives in USA
        (membero, ('Matthew', var(), var(), 'USA'), people),

        # The person who has a black car lives in Australia
        (membero, (var(), var(), 'black', 'Australia'), people),

        # The person with yellow cap lives in USA
        (membero, (var(), var(), 'yellow', 'USA'), people),

        # The person who lives in canada has green cat
        (membero, (var(), 'cat', 'green', 'Canada'), people),

        # Jack has a cat
        (membero, ('Jack', 'cat', var(), var()), people),

        # Alfred lives in Australia
        (membero, ('Alfred', var(), var(), 'Australia'), people),

        # Person who owns the dog lives in France
        (membero, (var(), 'dog', var(), 'France'), people),

        # Who has a rabbit?
        (membero, (var(), 'rabbit', var(), var()), people),

        # Who has a parrot?
        (membero, (var(), 'parrot', var(), var()), people)
    )

solutions = run(1, people, rules)
#print(solutions)

# Extract output
rabbit_owner = [house for house in solutions[0] if 'rabbit' in house][0][0]
parrot_owner = [house for house in solutions[0] if 'parrot' in house][0][0]
#print(output[0])
print('\n'+rabbit_owner+' is the owner of the rabbit')
print('\n'+parrot_owner+' owns the parrot')
print('\nHere are all the details:')
attribs = ['Name', 'Pet', 'Color', 'Country']
print('\n'+'\t\t'.join(attribs))
print('='*57)
for item in solutions[0]:
    print('')
    print('\t\t'.join([str(x) for x in item]))