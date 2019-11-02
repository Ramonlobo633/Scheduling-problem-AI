import hill_climb, steepest_ascent_hill_climbing, best_first_search


class Technique:
    def __init__(self, allocation, nurses=10):
        self.option = 0 
        self.allocation = allocation
        self.nurses = nurses

    def controller(self, opt=1):
        self.option = opt
        
        print('option: ', self.option)

        if self.option == 1:
            print('Executing Hill Climb technique')
            t = hill_climb.hill_climb_technique()
            t.hc(self.allocation, self.nurses)
            

        elif self.option == 2:
            print('Executing Steepest ascent hill climbing')
            sa = steepest_ascent_hill_climbing.steepest_ascent_hill_climb_technique()
            sa.sahc(self.allocation, self.nurses)

        elif self.option == 3:
            print('Executing Best first search')
            bf = BreadthFirstSearch.BreadthFirst(self.number)
            bf.bfs()
    
    
def output(title, allocation, conflits, nurses_number=10):
    print(title)
    for i in range(0, 21*nurses_number, 21):
        print(allocation[i:(i + 21)])
    print('Number of violated restrictions: ', conflits, '\n')

def state_generator(state, bit, nurses_number=10):
    new_state = state[0:bit]
    if state[bit] == '0':
        new_state += '1'
    else:
        new_state += '0'
    new_state += state[bit+1:21*nurses_number]

    return new_state, (bit + 1)