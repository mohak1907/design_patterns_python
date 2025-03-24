from transitions import Machine

states = ['solid', 'liquid', 'gas']
machine = Machine(states=states, initial='solid')
machine.add_transition('melt', 'solid', 'liquid')
machine.add_transition('evaporate', 'liquid', 'gas')

print(machine.state)  # Output: solid
machine.melt()
print(machine.state)  # Output: liquid
machine.evaporate()
print(machine.state)  # Output: gas