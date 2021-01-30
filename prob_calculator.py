from random import randint


class Hat:
    """
    Class representing a hat containing balls of different colors.
    It also has a method for drawing a certain number of balls from the hat
    without replacement.
    """

    def __init__(self, **balls):
        # ex.: balls = {red: 2} --> contents = [red, red]
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
            contents = self.contents.copy()  # so the original hat won't be affected
            results = []
            for i in range(balls_to_draw):
                drawn_ball = randint(0, len(contents) - 1)
                # record what ball has been drawn from the hat, removing it
                # from the hat.
                results.append(contents.pop(drawn_ball))

        return results















# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
