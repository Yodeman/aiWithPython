from kanren import run, var, fact
import kanren.assoccomm as ka

# Define mathematical operations
add = 'addition'
mul = 'multiplication'

# Declare that these operations are commutative using fact system
fact(ka.commutative, mul)
fact(ka.commutative, add)
fact(ka.associative, add)
fact(ka.associative, mul)

a, b, c = var('a'), var('b'), var('c')

# Generate expression
expression_orig = (add, (mul, 3, -2), (mul, (add, 1, (mul, 2, 3)), -1))
expression1 = (add, (mul, (add, 1, (mul, 2, a)), b), (mul, 3, c))
expression2 = (add, (mul, c, 3), (mul, b, (add, (mul, 2, a), 1)))
expression3 = (add, (add, (mul, (mul, 2, a), b), b), (mul, 3, c))

# Compare expressions
print(run(0, (a, b, c), ka.eq_assoccomm(expression1, expression_orig)))
print(run(0, (a, b, c), ka.eq_assoccomm(expression2, expression_orig)))
print(run(0, (a, b, c), ka.eq_assoccomm(expression3, expression_orig)))