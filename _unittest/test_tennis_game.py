# python -m unittest _unittest\test_tennis_game.py

import unittest
from tennis_game import TennisGame


class TestTenisGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = TennisGame()

    def test_something(self):
        self.assertEqual("Love all", self.game.score)

    def test_score_is_15_0_when_p1_scored_once(self):
        self.game.player_one_scored()
        self.assertEqual('Fifteen Love', self.game.score)

    def test_score_is_15_30_when_p1_scored_onceand_p2_scored_twice(self):
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_two_scored()
        self.assertEqual('Fifteen Thirty', self.game.score)

    def test_score_is_30_0_when_p1_scored_twice(self):
        self.game.player_one_scored()
        self.game.player_one_scored()
        self.assertEqual('Thirty Love', self.game.score)

    def test_score_is_30_15_when_p1_scored_twice_and_p2_scored_once(self):
        self.game.player_one_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.assertEqual('Thirty Fifteen', self.game.score)

    def test_score_is_40_15_when_p1_scored_three_and_p2_scored_once(self):
        self.game.player_one_scored()
        self.game.player_one_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.assertEqual('Forty Fifteen', self.game.score)

    def test_score_is_0_15_when_p2_scored_once(self):
        self.game.player_one_scored()
        self.assertEqual('Fifteen Love', self.game.score)

    def test_score_is_0_30_when_p2_scored_twice(self):
        self.game.player_two_scored()
        self.game.player_two_scored()
        self.assertEqual('Love Thirty', self.game.score)

    def test_score_is_0_40_when_p2_scored_three(self):
        self.game.player_two_scored()
        self.game.player_two_scored()
        self.game.player_two_scored()
        self.assertEqual('Love Forty', self.game.score)
