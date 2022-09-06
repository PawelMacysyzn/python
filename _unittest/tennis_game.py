

class TennisGame:
    def __init__(self) -> None:
        self.score = "Love all"
        self._p1_score = 0
        self._p2_score = 0

    def player_one_scored(self):
        self._p1_score += 1
        self.score = self._calculate_score()

    def player_two_scored(self):
        self._p2_score += 1
        self.score = self._calculate_score()

    def _calculate_score(self) -> str:
        if self._p1_score <= 3:
            first_result = self._translate_score(self._p1_score)
        elif self._p1_score == 4:
            return 'Game for P1'

        if self._p1_score == self._p2_score:
            return f"{first_result} all"

        if self._p2_score <= 3:
            second_result = self._translate_score(self._p2_score)
        elif self._p2_score == 4:
            return 'Game for P2'

        return f'{first_result} {second_result}'

    def _translate_score(self, player_score):
        if player_score == 0:
            return 'Love'
        elif player_score == 1:
            return 'Fifteen'
        elif player_score == 2:
            return 'Thirty'
        elif player_score == 3:
            return 'Forty'
