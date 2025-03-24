from transitions.extensions import HierarchicalMachine

class ATM:
    def enter_pin(self): print("PIN entered.")
    def withdraw(self): print("Cash withdrawn.")

atm = ATM()
states = ['idle', {'name': 'active', 'children': ['entering_pin', 'transacting']}]
machine = HierarchicalMachine(model=atm, states=states, initial='idle')

machine.add_transition('start', 'idle', 'active_entering_pin')
machine.add_transition('enter', 'active_entering_pin', 'active_transacting', after='enter_pin')
machine.add_transition('withdraw', 'active_transacting', 'idle', after='withdraw')

atm.start()
atm.enter()
atm.withdraw()
