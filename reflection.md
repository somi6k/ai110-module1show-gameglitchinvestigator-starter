# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
The suggestion will incorrectly suggest going Lower even if the secret is a higher number. In other instances it will suggest going higher when the current guess is already higher than the secret. Upon finishing a game, the New Game button does not work. The game also quits out of attempts even though there are more attempts remaining. When switching difficutly level, game still allows numbers outside for stated range.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input               | Expected Behavior      | Actual Behavior | Console Output / Error |
|---------------------|------------------------|-----------------|------------------------|
| 44                  |  Too High hint            Too low hint        None
| New Game            |  New game to start        Nothing happens     None
| Guess 7 Submitted   |  Another attempt allowed     No more attempts     Out of attempts!    
| Set to Hard            Range limited to 1-20      accepts 33 as input          None  

---

## 2. How did you use AI as a teammate?
I used Claude on this project to help write tests, fix bugs and write tests to verify. For the high/low bug, AI suggested to reverse the labels, stop casting the secret int to a string and then remove the unnecessary try/catch block.

One example of AI correctly suggesting a bug fix was the identification of the attempts counter starting at 1 instead of 0. This prevented the user from receiving the number of tries as per the difficulty level. I verified the correctness by running the game, as well as having the AI write a unit test which passed successfully. 

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
