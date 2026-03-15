from logic_utils import check_guess, parse_guess
from streamlit.testing.v1 import AppTest

# FIX: updated the return of the check_guess function to accept a tuple of (outcome, message)
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncated():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert err is None

def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is False
    assert value is None
    assert err == "Guess must be a positive number."

def test_parse_guess_large_negative():
    ok, value, err = parse_guess("-50")
    assert ok is False
    assert value is None
    assert err == "Guess must be a positive number."

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_letters_only():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_mixed_alphanumeric():
    ok, value, err = parse_guess("12abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_whitespace_only():
    ok, value, err = parse_guess("   ")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_special_characters():
    ok, value, err = parse_guess("!@#")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

# FIX: added a test to verify that hitting enter on the guess input field submits the form and increments attempts
def test_form_submit_processes_guess():
    # Verify that submitting the guess form increments attempts,
    # confirming the st.form fix allows Enter-key submission to work.
    at = AppTest.from_file("app.py").run()
    initial_attempts = at.session_state["attempts"]
    at.text_input[0].set_value("42")
    at.button[0].click().run()
    assert at.session_state["attempts"] == initial_attempts + 1
