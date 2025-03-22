import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents = []
            return drawn_balls
        
        drawn_balls = []
        for _ in range(num_balls):
            ball_index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(ball_index))
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        
        # Draw the balls
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Check if the drawn balls match the expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    # Calculate and return the probability
    return successful_experiments / num_experiments