import streamlit as st
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    chars = ""
    if use_letters: chars += string.ascii_letters
    if use_numbers: chars += string.digits
    if use_symbols: chars += string.punctuation
    
    if not chars:  # Default to letters if nothing selected
        chars = string.ascii_letters
        
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Generator")
password_length = st.slider("Password Length", 6, 32, 12)
use_letters = st.checkbox("Include Letters", value=True)
use_numbers = st.checkbox("Include Numbers")
use_symbols = st.checkbox("Include Symbols")

if st.button("Generate Password"):
    password = generate_password(password_length, use_letters, use_numbers, use_symbols)
    st.subheader("Generated Password:")
    st.code(password, language="text")
