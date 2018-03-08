
class Score:
    p1_score = 0
    p2_score = 0

    score_names = {
        0: 'love',
        1: 'fifteen',
        2: 'thirty',
        3: 'forty',
    }

    advantage = None

    def player_one_scores(self):
        if self.p1_score < 4:
            self.p1_score += 1

    def player_two_scores(self):
        if self.p2_score < 4:
            self.p2_score += 1

    def get_score(self):
        if self.p1_score + self.p2_score >= 6:
            return 'Deuce'
        if self.p1_score > 3:
            return 'Player 1 wins!!!'
        if self.p2_score > 3:
            return 'Player 2 wins!!!'
        return '{p1} x {p2}'.format(p1=self.score_names[self.p1_score],
                                    p2=self.score_names[self.p2_score])
