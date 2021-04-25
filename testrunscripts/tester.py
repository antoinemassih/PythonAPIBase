import ast

formula = 'value1 * 5 + value_2 /4'
names = [
    node.id for node in ast.walk(ast.parse(formula))
    if isinstance(node, ast.Name)
]

operators = [
    nard.id for nard in ast.walk(ast.parse(formula))
    if isinstance(nard, ast.)
]
print(operators)
print(names)
