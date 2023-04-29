import common.AFD as AFD

Q = AFD.Q
SIGMA = AFD.SIGMA
DELTA = AFD.DELTA
q0 = AFD.q0
F = AFD.F

def afd_to_glc(Q, SIGMA, DELTA, q0, F):
    # Paso 1: Agregar un nuevo símbolo de inicio S0 y una nueva regla S0 -> S
    S0 = 'S0'
    S = 'S'
    rules = {S0: [S]}

    # Paso 2: Agregar reglas para producir cadenas correspondientes a las posibles transiciones
    for q in Q:
        A_q = 'A_' + q
        for c in SIGMA:
            if c in DELTA[q]:
                r = DELTA[q][c]
                A_r = 'A_' + r
                if A_q not in rules:
                    rules[A_q] = []
                rules[A_q].append(c + A_r)

    # Paso 3: Agregar reglas para los estados finales
    for q in F:
        A_q = 'A_' + q
        if A_q not in rules:
            rules[A_q] = []
        rules[A_q].append('epsilon')

    # Paso 4: Eliminar transiciones epsilon
    epsilon_rules = {}
    for A in rules:
        for i in range(len(rules[A])):
            rule = rules[A][i]
            if rule == 'epsilon':
                epsilon_rules[A] = True
                rules[A].remove(rule)
                break
    for A in rules:
        for i in range(len(rules[A])):
            rule = rules[A][i]
            for B in epsilon_rules:
                if B in rule:
                    new_rule = rule.replace(B, '')
                    if new_rule != '':
                        rules[A].append(new_rule)

    # Paso 5: Simplificar la GLC
    useful_variables = {S}
    while True:
        old_size = len(useful_variables)
        for A in rules:
            if A in useful_variables:
                for rule in rules[A]:
                    for c in rule:
                        if c.isupper():
                            useful_variables.add(c)
        if len(useful_variables) == old_size:
            break
    
    simplified_rules = {A: [rule] for A in useful_variables for rule in rules[A] if len(rule) == 1 and rule.islower()}
    while True:
        old_size = len(simplified_rules)
        for A in rules:
            if A in useful_variables:
                for rule in rules[A]:
                    if all(c in simplified_rules for c in rule):
                        if A not in simplified_rules:
                            simplified_rules[A] = []
                        simplified_rules[A].append(rule)
        if len(simplified_rules) == old_size:
            break
    
    for A in rules:
        if A in useful_variables:
            simplified_rules[A] = simplified_rules.get(A, []) + [rule for rule in rules[A] if len(rule) > 1 or not rule.islower()]
    
    for A in simplified_rules:
        for i in range(len(simplified_rules[A])):
            rule = simplified_rules[A][i]
            new = ''
            for c in rule:
                if c.isupper():
                    new = new + '(' + simplified_rules[c][0] + ')'
                else:
                    new = new + c
            simplified_rules[A][i] = new
    
    return S0, S, simplified_rules