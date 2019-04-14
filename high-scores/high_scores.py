class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        return sorted(self.scores, reverse=True) [:3]

    def report(self):
        if self.scores[-1] < max(self.scores):
            difference = max(self.scores) - self.scores[-1]
            message = "That's {} short of your personal best!".format(difference)
        else:
            message = "That's your personal best!"
        return "Your latest score was {}. {}".format(self.scores[-1], message)
 
