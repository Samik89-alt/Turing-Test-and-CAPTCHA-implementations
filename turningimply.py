import random
import threading
import time
from groq import Groq

# ---------- API KEY ----------
client = Groq(api_key="YOUR_GROQ_API_KEY")  # Replace with your actual API key


# ---------- TIMER FUNCTION ----------
def input_with_timeout(prompt, timeout):

    answer = [None]

    def get_input():
        answer[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.start()

    thread.join(timeout)

    if thread.is_alive():
        return None
    return answer[0]


# ---------- GAME START ----------
score = 0
round_num = 1

print("\n==============================")
print("       HUMAN OR AI GAME")
print("==============================")
print("Guess if the response is HUMAN or BOT.")
print("You have 10 seconds to answer each round.")
print("Game ends when you guess wrong.\n")


while True:

    print(f"\n----- ROUND {round_num} -----")

    role = random.choice(["human", "bot"])

    question = input("\nAsk a question: ")

    # ---------- PROMPTS ----------
    if role == "human":

        prompt = f"""
        You are pretending to be a casual human.
        Speak naturally, slightly informal, maybe unsure.
        You may use casual words like "hmm", "yeah", "maybe".
        Keep the response under 2 sentences.

        Question: {question}
        """

    else:

        prompt = f"""
        You are an AI assistant.
        Respond logically and formally like a machine.
        Be structured and clear.
        Keep the response under 2 sentences.

        Question: {question}
        """

    # ---------- GROQ RESPONSE ----------
    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content

        print("\nResponse:")
        print(reply)

    except Exception as e:

        print("API Error:", e)
        print("Retrying in 10 seconds...")
        time.sleep(10)
        continue


    # ---------- TIMER INPUT ----------
    guess = input_with_timeout(
        "\nWas that HUMAN or BOT? (h/b): ",
        10
    )

    if guess is None:
        print("\n⏰ Time's up!")
        break

    guess = guess.lower()

    if (guess == "h" and role == "human") or (guess == "b" and role == "bot"):

        score += 1
        print("\nCorrect!")

    else:

        print("\nWrong guess!")
        print("Actual role:", role.upper())
        break

    round_num += 1

    time.sleep(2)


# ---------- FINAL SCOREBOARD ----------
print("\n==============================")
print("         GAME OVER")
print("==============================")
print("Rounds Survived:", score)
print("==============================")