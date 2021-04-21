from csp import *
import random

random.seed("aima-python")

# CSP Mapa Australia

neighbors = 'SA: WA Q NSW V NT; NT: WA Q; NSW: Q V; V: T; T: '
australia_coloring = MapColoringCSP(list('RGB'), 'SA: WA Q NSW V NT; NT: WA Q; NSW: Q V; V: T; T: ')

# {'SA': 'B', 'WA': 'R', 'Q': 'R', 'NSW': 'G', 'V': 'R', 'NT': 'G', 'T': 'B'}

print(min_conflicts(australia_coloring, 1000))

# Backtrack Search Mapa Australia

# {'SA': 'R', 'WA': 'G', 'Q': 'G', 'NSW': 'B', 'V': 'G', 'NT': 'B', 'T': 'R'}
print(backtracking_search(australia_coloring))
