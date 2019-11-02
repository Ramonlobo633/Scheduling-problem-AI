import scheduling as s, constraints as c

class steepest_ascent_hill_climb_technique:
    def __ini__(self):
       
    def sahc(self, allocation, nurses=10):         
        current_conflits = c.conflits(allocation, nurses)
        s.output('Inicial state', allocation, current_conflits, nurses)
        
        bit_position = 0
        if(current_conflits == 0):
            s.output('Objective state found ', allocation, current_conflits, nurses)
            return 

        last_state = allocation
        last_conflit = current_conflits

        while True:              
            loop = True

            while loop:

                if bit_position == nurses:
                    print('There is no new operators to be applied')
                    s.output('Last best state found', last_state, current_conflits, nurses)
                    return

                allocation, bit_position = s.state_generator(last_state, bit_position, nurses)
                current_conflits = c.conflits(allocation, nurses)
                
                if current_conflits < last_conflit:
                    state_loop = False
                    bit_position = 0

            if current_conflits == 0:
                s.output('Objective state found', allocation, current_conflits, nurses)
                return

            s.output('State generated', allocation, current_conflits, nurses)

            last_conflit = current_conflits
            last_state = allocation
                            
                            

