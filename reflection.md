# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- Mostly functional on a surface level, but faulty.
--- The "New Game" button didn't start a new game. The hints were backwards; the app tells the user to go higher when they're actually supposed to go lower and vice versa. When switching between difficulties, the range and number of attempts given in the instructions were wrong. "Attempts left" doesn't update properly for the first attempt.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- Copilot 
--- It suggested editing the hardcoded range shown to player to the range represented by the low and high variables. It was correct because the range is supposed to change according to the difficulty picked by player, and those variables get the range picked by player from the function get_range_for_difficulty(). Verified by running the app and checking if the range displayed changed with difficulty. 
--- One of the tests it generated called the check_guess() function and expected a string instead of a tuple. Test failed. Fixed the error itself when prompted and verified by running the tests.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- By testing the game with different combinations of player input.
--- Using pytest, test_winning_guess() checks that when the player's guess and the secret number match, it's a win.
--- Yes, it came up with all the tests in test_game_logic.py and used comments in the functions to explain what the tests do.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
