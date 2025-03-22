from prob_calculator import Hat, experiment

def main():
    # Example 1: Original problem from the instructions
    hat1 = Hat(blue=5, red=4, green=2)
    probability1 = experiment(
        hat=hat1,
        expected_balls={"red": 1, "green": 1},
        num_balls_drawn=5,
        num_experiments=2000
    )
    print("\nExample 1: Draw 5 balls, need at least 1 red and 1 green")
    print(f"Probability: {probability1:.4f}\n")
    
    # Example 2: More complex experiment
    hat2 = Hat(black=6, red=4, green=3)
    probability2 = experiment(
        hat=hat2,
        expected_balls={"red": 2, "green": 1},
        num_balls_drawn=5,
        num_experiments=5000
    )
    print("Example 2: Draw 5 balls from hat with 6 black, 4 red, 3 green")
    print("Need at least 2 red and 1 green")
    print(f"Probability: {probability2:.4f}\n")
    
    # Example 3: Very low probability
    hat3 = Hat(blue=20, red=10, green=15, yellow=5)
    probability3 = experiment(
        hat=hat3,
        expected_balls={"blue": 5, "red": 3, "green": 2},
        num_balls_drawn=10,
        num_experiments=10000
    )
    print("Example 3: Draw 10 balls from hat with 20 blue, 10 red, 15 green, 5 yellow")
    print("Need at least 5 blue, 3 red, and 2 green")
    print(f"Probability: {probability3:.4f}\n")
    
    # Example 4: Case where drawing exceeds available balls
    hat4 = Hat(red=5, blue=2)
    probability4 = experiment(
        hat=hat4,
        expected_balls={"red": 3},
        num_balls_drawn=10,  # More than total balls in hat
        num_experiments=1000
    )
    print("Example 4: Draw 10 balls from hat with only 7 balls (5 red, 2 blue)")
    print("Need at least 3 red")
    print(f"Probability: {probability4:.4f}\n")

if __name__ == "__main__":
    main()