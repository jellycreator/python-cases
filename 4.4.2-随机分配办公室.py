import random

teacher = [['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H']]

for i in range(len(teacher)):
    teacher[i].append(random.choice(['一号办公室','二号办公室','三号办公室']))

for i in range(len(teacher)):
    print(teacher[i])