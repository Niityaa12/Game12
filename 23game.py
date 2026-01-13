# # #guess
# # import random
# # def play_game():
# #     number = random.randint(1,100)
# #     attempts = 0

# #     while True:
# #         guess =int(input('enter you number:'))
# #         attempts+=1
# #         if guess < number:
# #             print('too low')
# #         elif guess > number:
# #             print("too high")
# #         else:
# #             print('golu won')
# #             print(attempts)
# #             break
# # play_game()





# import tkinter as tk
# import random

# class GuessGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Guess the Number")
#         self.root.geometry("300x250")

#         self.number = random.randint(1, 100)
#         self.attempts = 0

#         tk.Label(root, text="Guess the Number (1–100)", font=("Arial", 12)).pack(pady=10)

#         self.entry = tk.Entry(root, font=("Arial", 12))
#         self.entry.pack(pady=10)

#         self.button = tk.Button(root, text="Guess", command=self.check_guess)
#         self.button.pack(pady=5)

#         self.result = tk.Label(root, text="", font=("Arial", 11))
#         self.result.pack(pady=10)

#     def check_guess(self):
#         try:
#             guess = int(self.entry.get())
#             self.attempts += 1

#             if guess < self.number:
#                 self.result.config(text="Too low")
#             elif guess > self.number:
#                 self.result.config(text="Too high")
#             else:
#                 self.result.config(
#                     text=f"Golu won!\nAttempts: {self.attempts}"
#                 )
#                 self.button.config(state="disabled")
#         except ValueError:
#             self.result.config(text="Enter a number only")

# root = tk.Tk()
# game = GuessGame(root)
# root.mainloop()




##STREAMLIT:


import streamlit as st
import random

st.title("🎯 Guess the Number")

# Initialize state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.won = False

# UI always visible
guess = st.number_input(
    "Enter a number (1–100)",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Too low")
    elif guess > st.session_state.number:
        st.warning("Too high")
    else:
        st.success("Golu won 🎉")
        st.write("Attempts:", st.session_state.attempts)
        st.balloons()  # 🎈 THIS is what you wanted
        st.session_state.won = True

if st.button("Reset"):
    st.session_state.number = random.randint(1, 100)