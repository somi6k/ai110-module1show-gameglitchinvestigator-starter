# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

This game's purpose is to provide the user a guessing game experience, where the user is given a pre-defined number of chances to guess a random number within a pre-defined rance according to the selected difficulty level.

The AI generated code had several bugs, including:
   1. The Lower/Higher hints being reversed
   2. The game counter starting at 1 instead of 0
   3. The appropriate number of chances being allocated according to the correct difficulty setting
   4. The new_game button not properly resetting the gameplay status

Fixes for all of the above bugs were applied and documented. The higher/lower messages were reversed along with the removal of unnecessary type casting. The game counter bug was corrected to start the game at 0 attempts, and the new_game button logic was modified so that the game status and history were also reset when the button was pushed.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User starts new game in normal mode
2. User enters 39 (Secret is 80)
3. Game states 'GO HIGHER'
4. User enters 66
5. Game states 'GO HIGHER'
6. User enters 96
7. Game states 'GO LOWER'
8. User enters 80
9. Game states 'Correct!' with a baloon animation

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
collected 9 items                                                                                                                                               

tests/test_game_logic.py::test_winning_guess PASSED                                                                                                       [ 11%]
tests/test_game_logic.py::test_guess_too_high_tells_player_to_go_lower PASSED                                                                             [ 22%]
tests/test_game_logic.py::test_guess_too_low_tells_player_to_go_higher PASSED                                                                             [ 33%]
tests/test_game_logic.py::test_check_guess_compares_numerically_not_lexicographically PASSED                                                              [ 44%]
tests/test_game_logic.py::test_player_gets_full_attempts_per_difficulty PASSED                                                                            [ 55%]
tests/test_game_logic.py::test_starting_at_one_loses_an_attempt_early PASSED                                                                              [ 66%]
tests/test_game_logic.py::test_new_game_restores_playable_status PASSED                                                                                   [ 77%]
tests/test_game_logic.py::test_new_game_works_after_a_win PASSED                                                                                          [ 88%]
tests/test_game_logic.py::test_new_game_keeps_score_across_games PASSED                                                                                   [100%]

====================================================================== 9 passed in 0.03s =======================================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
