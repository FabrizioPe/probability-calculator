"""
I don't agree with the test "test_hat_draw": it enforces the class method
"draw" to eliminate the balls drawn from the hat. This way, the action of
putting the balls back into the hat at the end of the single experiment is not
modelled, and consequently a copy of the hat has to be done inside the
experiment function, at each iteration.
"""

import copy
import random


class Hat:
    """
    Class representing a hat containing balls of different colors.
    It also has a method for drawing a certain number of balls from the hat
    without replacement.
    """

    def __init__(self, **balls):
        # ex.: balls = {red: 2, blue: 1} --> contents = [red, red, blue]
        self.contents = list()
        for ball_color, ball_num in balls.items():
            self.contents += [ball_color] * ball_num

    def draw(self, balls_to_draw):
        """
        Randomly draw a number of balls from the hat.
        Return a list of the balls drawn.
        """
        if balls_to_draw >= len(self.contents): return self.contents;
        else:
            results = []
            for i in range(balls_to_draw):
                drawn_ball = random.randint(0, len(self.contents) - 1)
                # record what ball has been drawn from the hat, removing it
                # from the hat.
                results.append(self.contents.pop(drawn_ball))

        return results


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Do the actual experiment and return the probability for a certain balls
    configuration.
    :param hat: an instance of the Hat class
    :param expected_balls: the expected configuration, as a dictionary
    :param num_balls_drawn: number of balls to draw each time
    :param num_experiments: number of times the balls have to be drawn
    :return: an estimate of the probability for expected_balls config.
    """

    success = 0 # the number of times we get expected_balls as result
    for i in range(num_experiments):
        # see note [1] for useful link:
        hatc = copy.deepcopy(hat)
        # draw the appropriate number of balls from the hat, randomly
        results = hatc.draw(num_balls_drawn)
        # analyse the results: compare results with expected_balls
        for ball, ball_repetition in expected_balls.items():
           if results.count(ball) < ball_repetition:
                break
        else:
            success += 1

    return success / num_experiments

# [1]: https://stackoverflow.com/questions/17246693/...
# ...what-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignment-oper
# explains the diff. between shallow and deep copy, so you can understand why it's needed here
