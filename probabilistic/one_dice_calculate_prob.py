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

def calculate_probability(throws, outcome):
    return sum([1 for i in throws if i == outcome])/len(throws)

if __name__ == "__main__":
    throws = simulate_throws(5, 100000)
    outcome = 1
    probability = calculate_probability(throws, outcome)
    print(f'The probability of obtaining a {outcome} is {probability}')
    print(f'The probability of not obtaining a {outcome} is {1-probability}')
