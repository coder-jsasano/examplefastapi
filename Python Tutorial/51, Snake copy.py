import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, num in balls.items() for _ in range(num)]
        #for color, num in balls.items():
            #self.contents.extend([color] * num)
    
    def draw(self, num_balls):
        if num_balls >= self.contents:
            return self.contents[:]
        drawn_balls = random.sample(self.contents, num_balls)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

     # Create a copy of the hat for each experiment
    for _ in range(num_experiments):
        hat_copy = Hat(**{ball: hat.contents.count(ball) for ball in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the balls in the drawn sample
        drawn_count = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}

        if all(drawn_count.get(ball,0) >= num for ball, num in expected_balls.items()):
            success_count += 1
    
    return success_count / num_experiments

hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
expected_balls={"red": 1, "green": 2},
num_balls_drawn=4,
num_experiments=2000)
print(probability)






    



    
