import streamlit as st
import os

# File to store the total
FILE_PATH = "total.txt"

# Function to load the total from file
def load_total():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return int(file.read())
    else:
        return 0

# Function to save the total to file
def save_total(total):
    with open(FILE_PATH, "w") as file:
        file.write(str(total))

# Load saved total on app start
if "total" not in st.session_state:
    st.session_state.total = load_total()

# UI
st.title("🧮 Persistent Daily Number Tracker")

number = st.number_input("Enter number to add", step=1)

if st.button("Add"):
    st.session_state.total += number
    save_total(st.session_state.total)  # Save to file

st.success(f"📊 Current Total: {st.session_state.total}")
