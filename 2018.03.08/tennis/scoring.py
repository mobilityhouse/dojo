class Score:
    score_names = {
        0: 'love',
        1: 'fifteen',
        2: 'thirty',
        3: 'forty',
    }

    def __init__(self, ):
        self.score = [0, 0]
        self.advantage = 0

    def _set_advantage(self, player):
        delta = [1, -1][player]
        if abs(self.advantage) < 2:
            self.advantage += delta

    def _player_scores(self, player):
        adversary = player ^ 1  # Bitwise exclusive or
        if self.score[player] <= 3:
            self.score[player] += 1
        if self.score[player] + self.score[adversary] > 6:
            self._set_advantage(player)

    def player_one_scores(self):
        self._player_scores(0)

    def player_two_scores(self):
        self._player_scores(1)

    def get_score(self):
        if self.score[0] + self.score[1] >= 6:
            if self.advantage == 0:
                return 'Deuce'
            if self.advantage == 1:
                return 'Advantage player 1'
            if self.advantage == -1:
                return 'Advantage player 2'
        if self.score[0] > 3 or self.advantage == 2:
            return 'Player 1 wins!!!'
        if self.score[1] > 3 or self.advantage == -2:
            return 'Player 2 wins!!!'
        return '{} x {}'.format(
            self.score_names[self.score[0]],
            self.score_names[self.score[1]],
        )
