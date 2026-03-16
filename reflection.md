# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The first time I loaded up the game, it looked completely fine. I was just playing around and tinkering with the different features of the game to get a feel for 
    what it was about. Based on my first impression, it seemed pretty put together. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    The first thing I noticed was that the hints did not make sense. When the number was too low, it said to go lower and when the number was too high, it said to go higher. So clearly, the hints were switched. Another bug I noticed was that the attempts initially started at 1 when no guesses had been made yet. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I used claude and Copilot. At first, I used Claude where I explained the problem and asked it where the specific problem was occuring. I did this because I wanted
    to look at the code for myself and try to figure it out on my own. Then, if I was unable to, I would ask the AI on how to fix the error and take its suggestion.
    Later on in the project, I switched to Copilot to write the test cases to ensure that all the glitches were fixed and the logic for the game was working properly.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    I told Claude "The attempts do not decrease after the first guess, only after the second one. What could be the cause of this?" to which it replied the specific lines of code that was the issue and suggested that the fix be to "move the st.info(...) display to after the if submit: block." I took this suggestion and verified it by playing the game and ensuring that the attempts decreased one time after every guess. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    For two test cases, they kept continuously failing and I was a bit confused since Copilot wrote the tests. I took a look at the test cases and it looked like the assertions were reversed. I asked the AI "take a look at the test for test_guess_too high and test_guess_too_low, why is it failing? I think it is the test itself" and it turned out that my hunch was correct. The AI affirmed that the assertions in the test cases were reversed and gave me the code for the correct behavior. Once I implemented this, all of the test cases passed. 



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    By first playing the game and testing different modes and numbers. After that, I made sure the test cases were all passing. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    I ran pytest on the test_game_logic.py file, which executed 18 unit tests for functions like check_guess and update_score. They all passed which confirmed that the refactored logic in logic_utils.py correctly fixed the glitches without breaking existing behavior.
- Did AI help you design or understand any tests? How?
    Yes, Copilot helped design the pytest tests by generating the initial tes.t cases based on the glitches documented in app.py, and it assisted in understanding why certain tests were failing

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Streamlit reruns are when the app script executes from top to bottom every time a user interacts with it by doing things such as clicking a button or changing an input. This allows the UI to update instantally without having to refresh manually. An example would be when a user clicks on the submit guess button and the different displays are updated such as the hints, attempts, or score. 
    Session state is like a storage that keeps data for the game throughout the current rerun so that the variables are not resetting every single time the app refreshes. An example would be the secret number or score.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    I really got into the habit of writing and running pytest tests after every major change, like refactoring functions or fixing glitches—it made me feel way more confident that my code wasn't breaking things, so I'll definitely keep doing that in future projects to catch issues early.
- What is one thing you would do differently next time you work with AI on a coding task?
    Next time, I'd double-check AI-generated test assertions right away instead of assuming they're correct, because I learned that even AI can mix up expected behaviors, and it saves a lot of debugging time.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    This project showed me that AI-generated code can be super helpful for speeding up tasks like writing tests or suggesting fixes, but it's not perfect and I need to understand and verify it myself to avoid sneaky bugs. It helped me see how I can use AI as a teammate and not just a replacement for my own thinking.
