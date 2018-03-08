import pytest

from tennis.scoring import Score


def test_initial_score():
    score = Score()
    assert score.get_score() == 'love x love'


@pytest.mark.parametrize('play, expected_score', [
    (1, 'fifteen x love'),
    (2, 'love x fifteen'),
])
def test_a_player_scores(play, expected_score):
    score = Score()
    if play == 1:
        score.player_one_scores()
    else:
        score.player_two_scores()
    assert score.get_score() == expected_score


@pytest.mark.parametrize('plays, expected_score', [
    ([1, 1, 1], 'forty x love'),
    ([2, 1, 2, 1],  'thirty x thirty'),
    ([1, 1, 1, 1], 'Player 1 wins!!!'),
    ([2, 2, 2, 2], 'Player 2 wins!!!'),
    ([2, 2, 2, 1, 1, 1], 'Deuce'),
    ([2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2], 'Deuce'),
    ([2, 2, 2, 1, 1, 1, 1], 'Advantage player 1'),
    ([2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1], 'Advantage player 1'),
    ([2, 2, 2, 1, 1, 1, 1, 1], 'Player 1 wins!!!'),
    ([2, 2, 2, 1, 1, 1, 2], 'Advantage player 2'),
    ([2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2], 'Advantage player 2'),
    ([2, 2, 2, 1, 1, 1, 2, 2], 'Player 2 wins!!!'),
])
def test_multiple_scores(plays, expected_score):
    score = Score()
    for play in plays:
        if play == 1:
            score.player_one_scores()
        else:
            score.player_two_scores()
    assert score.get_score() == expected_score
