import scheduling as s, constraints as c

class best_first_search_technique:
    def __ini__(self):
        
        self.bit_position = 0
    def bfs(self, allocation, nurses=10):      
        list_open = list()
        initial_state = allocation   
        current_conflits = c.conflits(initial_state, nurses)
        s.output('Inicial state', initial_state, current_conflits, nurses)
        list_open.append(initial_state)
        bit_position = 0
        
        
        best_state = initial_state
        best_conflits = current_conflits

        while True:              
          
            while len(list_open) > 0:

                for i in range(0, len(list_open)):
                    current_state = list_open[0]
                    if c.conflits(current_state, nurses) < c.conflits(best_state, nurses):
                        best_state = current_state
                    list_open.pop(i)
               
                while bit_position != nurses:
                    current_state, bit_position = s.state_generator(current_state, bit_position, nurses)
                    if current_state in list_open:
                        list_open.append(current_state)
                        last_state = current_state
                    else:
                        if c.conflits(current_state, nurses) < c.conflits(best_state, nurses):
                            last_state = current_state
                            best_state = current_state

                bit_position = 0

                
                if c.conflits(best_state, nurses) == 0:
                    s.output('Objective state found', current_state, c.conflits(best_state, nurses), nurses)
                    return

               
                    

            if current_conflits == 0:
                s.output('Objective state found', target_state, c.conflits(best_state, nurses), nurses)
                return
            s.output('Last best state found', best_state, c.conflits(best_state, nurses), nurses)
            return    

           
                            
                            

