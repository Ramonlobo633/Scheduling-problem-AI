import scheduling as s, constraints as c, random as r, decimal as d

       
population = list()
population_number = 10
max_generation = 3

def ga(allocation, nurses=10):    
    current_conflits = c.conflits(allocation, nurses)
    s.output('Inicial state', allocation, current_conflits, nurses)
       
    initial_population = population_generator(population_number, nurses)
    current_population = initial_population
    shots = 0
    
    while shots < max_generation:
    
        count = 0
        population_fits = []
        while count != population_number:
            population_fits.append(fitness_func(current_population[count], nurses))
            
            if fitness_func(current_population[count], nurses) == 1:
                s.output('Objective state found', current_population[count], 0, nurses)
                return
            count += 1
        
        best_fits = sorted(population_fits, reverse=True)
        id_state = 0
        count = 0
        i = 0
        aux = population_number
        raking = []
        while count != population_number:
            id_state = population_fits.index(best_fits[count])
            aux = population_number - count
            while aux > 0:
                raking.append(id_state)
                i += 1
                aux -= 1

            count += 1
        id_state = population_fits.index(best_fits[0])
        best_state = current_population[id_state]

        id_state = population_fits.index(best_fits[1])
        best_state2 = current_population[id_state]
       
        current_population = new_generation(raking, current_population, nurses)
        current_population.insert(0, best_state)
        current_population.insert(1, best_state2)


        shots += 1
                        
    print('There is no new operators to be applied')
    s.output('Last best state found', making_str(best_state, nurses), c.conflits(best_state, nurses), nurses)
    return                  

def population_generator(population_number, nurses):
    population = []
    state = ''
    while population_number > 0:

        for i in range(0, 21*nurses):
            state = state + str(r.randrange(0, 2))     
                
        population.append(state)
        population_number -= 1

    return population

def fitness_func(state, nurses):
    fit = 0
    max_conflit = nurses + nurses * 5 + 21

    state_conflit = c.conflits(state, nurses)

    if state_conflit == fit:
        return 1.0 
    fit = (1/d.Decimal(max_conflit)) * state_conflit

    return round(1 - fit, 2)

def new_generation(ranking, current_population, nurses):
    new_generation = []
    count = 2
    while count != population_number:
        selected_id1 = r.randrange(0, len(ranking))
        selected_id2 = r.randrange(0, len(ranking))

        selected_state1 = current_population[ranking[selected_id1]]
        selected_state2 = current_population[ranking[selected_id2]]

        crossover_state = crossover(selected_state1, selected_state2, nurses)
        mutation_state = mutation(crossover_state, nurses)

        new_generation.append(crossover_state)
        new_generation.append(mutation_state)
        count += 1
    return new_generation

def crossover(state1, state2, nurses):
    new_state = list()
    max_bits = nurses*21
    bit_position = 0
    while bit_position != max_bits:
        new_state.append(state1[bit_position])
        if bit_position >= (max_bits/2):
            new_state.append(state2[bit_position])
        bit_position += 1
    str(new_state)
    return new_state

def mutation(state, nurses):
    new_state = list()
    max_bits = nurses*21
    bit_position = 0
    while bit_position != max_bits:
        new_state.append(state[bit_position])
        
        if bit_position >= (max_bits/2):
            new_state.append(r.randrange(0, 2))
        bit_position += 1
    str(new_state)
    return new_state
def making_str(state, nurses):
    string  = ''
    for i in range(0, 21*nurses):
        string = string + str(state[i])  
    return string 
