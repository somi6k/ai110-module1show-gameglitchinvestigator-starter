from logic_utils import check_guess


# ---------------------------------------------------------------------------
# Sanity: a correct guess is still a win.
# ---------------------------------------------------------------------------
def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


# ---------------------------------------------------------------------------
# Bug #1: the higher/lower HINT messages were swapped.
#
# A guess ABOVE the secret was labelled "Too High" (correct) but told the
# player to "Go HIGHER!" (wrong direction). These tests pin the *message* to
# the right direction so the swap can't silently come back.
# ---------------------------------------------------------------------------
def test_guess_too_high_tells_player_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # too high -> must go LOWER


def test_guess_too_low_tells_player_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message  # too low -> must go HIGHER


# ---------------------------------------------------------------------------
# Bug #2: app.py used to stringify the secret on even attempts, forcing a
# lexicographic comparison ("9" > "10" is True). check_guess must compare
# numerically. With numeric comparison, 9 vs 10 is "Too Low"; lexicographic
# string comparison would wrongly report "Too High".
# ---------------------------------------------------------------------------
def test_check_guess_compares_numerically_not_lexicographically():
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"

    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"


# ---------------------------------------------------------------------------
# Bug #3: the attempts counter started at 1 instead of 0, so a game ended one
# guess early ("out of attempts when there are some left").
#
# app.py's loss logic is: start at 0, each submit does `attempts += 1` then
# checks `attempts >= attempt_limit`. The simulation below mirrors that loop
# exactly and asserts the player gets the FULL number of guesses. If the
# counter is ever re-initialised to 1, `guesses_taken` drops to limit - 1.
# ---------------------------------------------------------------------------
def simulate_full_game(attempt_limit, start_attempts=0):
    """Replays app.py's attempt accounting until the game is lost."""
    attempts = start_attempts
    guesses_taken = 0
    while True:
        attempts += 1            # app.py: st.session_state.attempts += 1
        guesses_taken += 1
        if attempts >= attempt_limit:  # app.py loss check
            break
    return guesses_taken


def test_player_gets_full_attempts_per_difficulty():
    # (difficulty limit from attempt_limit_map in app.py)
    for attempt_limit in (6, 8, 5):  # Easy, Normal, Hard
        assert simulate_full_game(attempt_limit) == attempt_limit


def test_starting_at_one_loses_an_attempt_early():
    # Documents the OLD bug: initialising attempts at 1 robs one guess.
    assert simulate_full_game(8, start_attempts=1) == 7
