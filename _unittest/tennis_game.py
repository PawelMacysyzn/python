class TennisGame:
    def __init__(self) -> None:
        self.score = "Love all"
        self.p1_score = 0
        self.p2_score = 0

    def player_one_scored(self):
        self.p1_score += 1
        self._calculate_score()

    def player_two_scored(self):
        self.p2_score += 1
        self._calculate_score()

    def _calculate_score(self):
        first_result, second_result = 'Love', 'Love'
        if self.p1_score == 1:
            first_result = 'Fifteen'
        elif self.p1_score == 2:
            first_result = 'Thirty'
        elif self.p1_score == 3:
            first_result = 'Forty'

        if self.p2_score == 1:
            second_result = 'Fifteen'
        elif self.p2_score == 2:
            second_result = 'Thirty'
        elif self.p2_score == 3:
            second_result = 'Forty'

        self.score = f'{first_result} {second_result}'
