from app import get_range_for_difficulty, parse_guess, check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low(): 
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")
def test_check_guess_with_str_secret():
    # Glitch in submit logic: on even attempts, secret is str, so check_guess with str secret
    # Should still win if guess matches, but due to TypeError, it returns "Too Low"
    result = check_guess(50, "50")
    # Expecting win, but glitch causes "Too Low"
    assert result == ("Win", "🎉 Correct!")

def test_get_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_get_range_normal():
    # Glitch #7: ranges for normal and hard are switched
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_get_range_hard():
    # Glitch #7: ranges for normal and hard are switched
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_get_range_default():
    assert get_range_for_difficulty("Invalid") == (1, 100)

def test_parse_guess_valid():
    ok, guess, err = parse_guess("50")
    assert ok == True
    assert guess == 50
    assert err == None

def test_parse_guess_float():
    ok, guess, err = parse_guess("50.0")
    assert ok == True
    assert guess == 50
    assert err == None

def test_parse_guess_empty():
    ok, guess, err = parse_guess("")
    assert ok == False
    assert guess == None
    assert err == "Enter a guess."

def test_parse_guess_none():
    ok, guess, err = parse_guess(None)
    assert ok == False
    assert guess == None
    assert err == "Enter a guess."

def test_parse_guess_invalid():
    ok, guess, err = parse_guess("abc")
    assert ok == False
    assert guess == None
    assert err == "That is not a number."

def test_update_score_win():
    assert update_score(0, "Win", 0) == 90  # 100 - 10 * (0 + 1) = 90

def test_update_score_win_min():
    assert update_score(0, "Win", 9) == 10  # 100 - 10*10 = 0, but min 10

def test_update_score_too_high_even_attempt():
    # Glitch: for even attempt_number, adds 5 instead of subtracting
    # Expecting -5 always
    assert update_score(0, "Too High", 1) == -5  # attempt 1 % 2 == 1, odd, -5

def test_update_score_too_high_odd_attempt():
    # attempt 0 % 2 == 0, even, code adds 5, but expect -5
    assert update_score(0, "Too High", 0) == -5

def test_update_score_too_low():
    assert update_score(0, "Too Low", 0) == -5
