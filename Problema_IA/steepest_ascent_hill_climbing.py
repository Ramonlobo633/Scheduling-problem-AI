import scheduling as s, constraints as c

class steepest_ascent_hill_climb_technique:
    def __ini__(self):
        
        self.bit_position = 0
    def sahc(self, allocation, nurses=10):      

        initial_state = allocation   
        current_conflits = c.conflits(initial_state, nurses)
        s.output('Inicial state', allocation, current_conflits, nurses)
        
        bit_position = 0
        

        if(current_conflits == 0):
            s.output('Objective state found ', allocation, current_conflits, nurses)
            return 
        target_state = allocation
        current_state = initial_state
        target_conflits = current_conflits

        while True:              
            loop = True

            while loop:

                if bit_position == nurses:
                    print('There is no new operators to be applied')
                    s.output('Last best state found', target_state, current_conflits, nurses)
                    return
                current_state, bit_position = s.state_generator(current_state, bit_position, nurses)
                current_conflits = c.conflits(current_state, nurses)
                 
                if current_conflits == 0:
                    s.output('Objective state found', current_state, current_conflits, nurses)
                    return
                elif current_conflits < target_conflits:
                    target_state = current_state
                    target_conflits = current_conflits
                else:
                    current_state = target_state
                    current_conflits = target_conflits

               
                    

            if current_conflits == 0:
                s.output('Objective state found', target_state, current_conflits, nurses)
                return
     
            

           
                            
                            

