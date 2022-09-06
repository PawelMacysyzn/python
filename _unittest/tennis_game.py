

class TennisGame:
    def __init__(self) -> None:
        # self._score = "Love all"
        self._p1_score = 0
        self._p2_score = 0

    @property
    def score(self):
        return self._calculate_score()

    def player_one_scored(self):
        self._p1_score += 1
        self._score = self._calculate_score()

    def player_two_scored(self):
        self._p2_score += 1
        self._score = self._calculate_score()

    def _calculate_score(self) -> str:

        if self._is_deuce():
            return 'Deuce'

        if self._p1_score >= 4 and self._p2_score >= 4 and self._p1_score - self._p2_score == 1:
            return 'Advantage P1'

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

    def _is_deuce(self):
        return self._p1_score >= 4 and \
            self._p2_score >= 4 and \
            self._p1_score == self._p2_score
