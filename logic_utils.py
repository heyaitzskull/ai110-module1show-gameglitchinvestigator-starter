def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""

    #glitch #7: the range mapping for Normal and Hard must match the intended design.
    #FIX: Used Copilot to correct the ranges for Normal and Hard difficulties to match the intended design and refractored the logic into logic_utils.py
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def _to_int_if_possible(value):
    """Attempt to normalize a value to int for comparison."""
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    if isinstance(value, str):
        try:
            if "." in value:
                return int(float(value))
            return int(value)
        except Exception:
            return value
    return value


def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message)."""

    #glitch #1: the higher/lower logic was not working correctly, it was switched up
    #FIX: Used Copilot to implement the correct logic for comparing the guess to the secret number
    guess_val = _to_int_if_possible(guess)
    secret_val = _to_int_if_possible(secret)

    if guess_val == secret_val:
        return "Win", "🎉 Correct!"

    #If we can compare numerically, do so; otherwise fall back to string comparison.
    try:
        if guess_val > secret_val:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except Exception:
        g = str(guess)
        s = str(secret)
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""

    #glitch #8: scoring was not consistent with the intended design
    #FIX: Used Copilot to implement the correct scoring logic based on the outcome and attempt number and refactored the logic into logic_utils.py
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    #Incorrect guesses always penalize the player.
    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    return current_score
