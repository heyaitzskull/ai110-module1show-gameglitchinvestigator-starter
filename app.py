import random
import streamlit as st

from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,

)

#glitch #11, the attempts are switched, should be easy: 8, normal: 6, hard: 5
#FIX: switched the numbers to the correct values for each difficulty level
attempt_limit_map = {
    "Easy": 8,
    "Normal": 6,
    "Hard": 5,
}

attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

#glitch #10,  the secret number is only set once when the session starts, so changing the difficulty doesn't update it to match the new range.
#FIX: Used Copilot to implement the logic to check if difficulty changed, and reset game state if so
if "difficulty" not in st.session_state or st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    #glitch #2, attempts start at 1 instead of 0
    #FIX: changed the attempts to start at 0, so the first guess will be attempt 1, and the count will be accurate for the user.
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

#glitch #6, no matter the difficulty, it always says "Guess a number between 1 and 100"
#FIX: Used Copilot to update the message to reflect the actual range based on the selected difficulty, using the low and high values obtained from get_range_for_difficulty() to dynamically display the correct range in the info message.
st.info(
    f"Guess a number between {low} and {high}. "
)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

#glitch #4, the "New Game" button does not reset the game state properly, so starting a new game does not update the secret number or reset attempts and score.
#FIX: Copilot suggested adding code to reset the game state (secret number, attempts, score, status, history) when the "New Game" button is pressed, and then rerunning the app to reflect the changes immediately.
if new_game:
    st.session_state.attempts = 0 # reset attempts to 0 for new game

    #glitch #5, the secret number range was always 1 to 100, when it should be based on the difficulty level selected.
    #FIX: Added if/elif to set the secret number based on the selected difficulty, using the appropriate range for each level. 
    if difficulty == "Easy":
        st.session_state.secret = random.randint(1, 20)
    elif difficulty == "Normal":
        st.session_state.secret = random.randint(1, 50)
    else:
        st.session_state.secret = random.randint(1, 100) 

    st.success("New game started.")
    st.session_state.status = "playing" #adding this to reset the game status to playing when starting a new game
    st.session_state.history = [] #reset history for new game
    st.session_state.score = 0 #reset score for new game
 
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        if st.session_state.attempts % 2 == 0:
            secret = str(st.session_state.secret)
        else:
            secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

#glitch #3, the attempt count is off by one because it increments after checking for win/loss, so the "Attempts left" message is always one less than it should be. 
#FIX: Copilot suggested moving st.info() to the bottom to reflect the actual attempts left
st.info(
    
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

#glitch #9, the developer debug info does not show the updated attempts, score, and history immediately after a guess is made
#FIX: Moved the developer debug info to the bottom to reflect the actual state of the game after the guess is processed
with st.expander("Developer Debug Info"):  
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
