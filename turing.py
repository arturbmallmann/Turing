left=-1
right=1
stop=0
class state():
    def __init__(self,name):
        self.name=name
        self.next=dict()

    def add_transaction(self,simbol,next_state,write,direction):
        self.next.update({simbol:(next_state,write,direction)})

    def compute(self,simbol):
        return self.next.get(simbol)

    def get_name(self):
        return self.name

class machine():
    def __init__(self,q0,states,tape):
        self.states=states
        astate=q0
        self.tape=tape
        self.position=0

    def add_state(self,state):
        self.append(states)

    def compute(self):
        pos=self.position
        (astate,
        self.tape[pos],
        self.position) = astate.compute(self.tape[self.position])        

def main():
    tape=['>',0,0,1,'U',1,0,0] 
    states=[state('q0'),
            state('q1')]
#    states[0].
if __name__=='__init__':
    main()
