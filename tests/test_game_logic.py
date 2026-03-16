from logic_utils import check_guess, get_range_for_difficulty, get_attempt_limit

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_messages():
    # Test that hint messages are correct and not backwards
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High"
    assert message_high == "📉 Go LOWER!"
    
    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low"
    assert message_low == "📈 Go HIGHER!"

def test_get_range_for_difficulty():
    # Test ranges for difficulties to ensure they are correct when switching
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    assert get_range_for_difficulty("Invalid") == (1, 100)  # default

def test_get_attempt_limit():
    # Test attempt limits for difficulties to ensure they are correct when switching
    assert get_attempt_limit("Easy") == 6
    assert get_attempt_limit("Normal") == 8
    assert get_attempt_limit("Hard") == 5
    assert get_attempt_limit("Invalid") == 8  # default