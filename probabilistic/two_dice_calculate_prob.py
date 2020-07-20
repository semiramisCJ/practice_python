import random

def throw_dice(n_throws):
    throw_sequence = []
    for _ in range(n_throws):
        throw = random.choice([1,2,3,4,5,6])
        throw_sequence.append(throw)
    return throw_sequence

def simulate_throws(n_throws, simulation_times):
    throws = []
    for _ in range(simulation_times):
        throw_sequence = throw_dice(n_throws)
        throws.extend(throw_sequence)
    return throws

def calculate_probability(throws_A, throws_B, outcome):
    res = [1 for i in range(len(throws_A)) 
            if throws_A[i] + throws_B[i] == outcome]
    return sum(res)/len(throws_A)

if __name__ == "__main__":
    throws_A = simulate_throws(5, 100000)
    throws_B = simulate_throws(5, 100000)
    outcome = 12
    probability = calculate_probability(throws_A, throws_B, outcome)
    print(f'The probability of obtaining a sum of {outcome} is {probability}')
