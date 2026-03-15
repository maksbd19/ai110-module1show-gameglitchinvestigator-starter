from logic_utils import check_guess
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

# FIX: added a test to verify that hitting enter on the guess input field submits the form and increments attempts
def test_form_submit_processes_guess():
    # Verify that submitting the guess form increments attempts,
    # confirming the st.form fix allows Enter-key submission to work.
    at = AppTest.from_file("app.py").run()
    initial_attempts = at.session_state["attempts"]
    at.text_input[0].set_value("42")
    at.button[0].click().run()
    assert at.session_state["attempts"] == initial_attempts + 1
