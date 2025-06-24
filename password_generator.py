import streamlit as st
import random
import string


def generate_password(length, use_letters, use_numbers, use_symbols):
    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:  # if nothing selected
        chars = string.ascii_letters

    # Ensuring at least one character from each selected category
    password_chars = []
    if use_letters:
        password_chars.append(random.choice(string.ascii_letters))
    if use_numbers:
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))

    # Filling the rest of the password length with random choices
    remaining_length = length - len(password_chars)
    password_chars.extend(random.choice(chars)
                          for _ in range(remaining_length))

    # Shuffling
    random.shuffle(password_chars)

    return ''.join(password_chars)


# Streamlit UI
st.title("🔐 Password Generator")
password_length = st.slider("Password Length", 6, 32, 12)
use_letters = st.checkbox("Include Letters", value=True)
use_numbers = st.checkbox("Include Numbers")
use_symbols = st.checkbox("Include Symbols")

if st.button("Generate Password"):
    password = generate_password(
        password_length, use_letters, use_numbers, use_symbols)
    st.subheader("Generated Password:")
    st.code(password, language="text")
