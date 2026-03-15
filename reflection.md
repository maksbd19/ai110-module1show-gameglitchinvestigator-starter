# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  -- The app ran without any error, the UI looked clean and intuitive. There was a clear message of what to do and the buttons and control elements were clearly labeled.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  -- After entering a number in the input, hitting enter key doesn't submit the guess despite the message saying "Press Enter to apply".
  -- The hints were problematic, they weren't consistent to the input to the secret.
  -- Clicking on the 'New Game' button should reset the game and start a new one.
  -- Submitting empty guess or invalid string decreases attempt left count and it goes to negative.
  -- The attempt value is inconsistent between the sidebar, top message and developer debug section
  -- Switching difficulty in the settings sidebar doesn’t change the secret or reset the game.
  -- Submitting negative number doesn't show any error
  -- Score calculation is problematic

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - In the UI changing the difficulty wasn't resetting the game. When I prompted this message in the chat, claude was able to find the root cause immediately. It correctly identified that the secret was being set once the app starts not taking account of the switch of difficulty. I accepted the changes and ran the UI to verify the fix.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - The history wasn't being updated when a guess was submitted. I asked Claude to debug the issue. It deleted the code where the history was being shown and argued that removal of the code resolves the problem. Then I asked it to find another way instead and it went into a rabbit hole. In a new chat I specifically asked what i wanted then the agent suggested to use st.rerun as the app runs top to bottom and history is already rendered before the submit handler was executed. I accepted this argument and verified the outcome in the UI

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I manually tested the UI and asked the agent to create some test cases which I verified after adding to the test suite.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - While fixing the bug with switching difficulty not resetting the game, I tested the UI manually and asked the agent to create a UI test case `test_difficulty_switch_resets_game` which I ran using pytest. I observed the game was being reset and the test suite passed.
- Did AI help you design or understand any tests? How?
  - I asked AI to come up some test cases for the `update_score` function. It was able to understand the logic behind the scoring and come up with some cases all by itself. It helped me to realize a case that I missed when I was manually testing the scoring.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
