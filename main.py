import random
import matplotlib.pyplot as plt
from math import comb

def simulate_random_walks(n_steps, n_trials):
    returns_to_origin = 0
    for _ in range(n_trials):
        pos = 0
        for _ in range(n_steps):
            pos += random.choice([-1, 1])
        if pos == 0:
            returns_to_origin += 1
    return returns_to_origin / n_trials

steps_range = list(range(2, 102, 2))
n_trials = 10000
simulated_probs = []
theoretical_probs = []

for n in steps_range:
    sim_prob = simulate_random_walks(n, n_trials)
    simulated_probs.append(sim_prob)
    k = n // 2
    theo_prob = comb(n, k) / (2 ** n)
    theoretical_probs.append(theo_prob)

plt.figure(figsize=(10, 6))
plt.plot(steps_range, simulated_probs, label='Simulated Probability', marker='o')
plt.plot(steps_range, theoretical_probs, label='Theoretical Probability', marker='x')
plt.xlabel('Number of Steps (n)')
plt.ylabel('Probability of Return to Origin')
plt.title('1D Random Walk: Probability of Returning to Origin')
plt.legend()
plt.grid(True)
plt.show()

n_steps = 100
n_paths = 10

plt.figure(figsize=(10, 6))

for _ in range(n_paths):
    pos = 0
    path = [pos]
    for _ in range(n_steps):
        pos += random.choice([-1, 1])
        path.append(pos)
    plt.plot(range(n_steps + 1), path, alpha=0.7)

plt.title('Sample Paths of 10 Random Walks (n = 100 steps)')
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.grid(True)
plt.show()