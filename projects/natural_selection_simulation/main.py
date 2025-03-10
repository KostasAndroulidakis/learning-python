"""Simulates natural selection in the fictional Neebler population."""

import random

# Starting population with each trait variation.
small_neeblers = 100
big_neeblers = 100

generation = 0
max_generations = 10

while small_neeblers > 0 and big_neeblers > 0 and generation < max_generations:
    for neebler in range(small_neeblers):
        # Low chance of being spotted by predators since they're small.
        chance_of_being_spotted = random.randint(0, 4)
        if chance_of_being_spotted == 4:
            small_neeblers = small_neeblers - 1
    
    baby_small_neeblers = 0
    for neebler in range(small_neeblers):
        # Smallness trait gets passed to their babies.
        num_small_babies = random.randint(0, 3)
        baby_small_neeblers = baby_small_neeblers + num_small_babies
    
    for neebler in range(big_neeblers):
        # Large chance of being spotted by predators since they're big.
        chance_of_being_spotted = random.randint(1, 4)
        if chance_of_being_spotted == 4:
            big_neeblers = big_neeblers - 3
    
    baby_big_neeblers = 0
    for neebler in range(big_neeblers):
        # Bigness trait gets passed to their babies.
        num_big_babies = random.randint(0, 3)
        baby_big_neeblers = baby_big_neeblers + num_big_babies
    
    
    # Babies become the starting population of the next generation.
    small_neeblers = baby_small_neeblers
    big_neeblers = baby_big_neeblers
    
    print(str(small_neeblers) + " small Neeblers")
    print(str(big_neeblers) + " big Neeblers")
    generation += 1
