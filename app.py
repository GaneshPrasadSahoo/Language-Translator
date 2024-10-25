import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit App Title
st.title("Language Translator by GP Projects🚀")

# Input Text Box
st.subheader("Enter Text to Translate:")
input_text = st.text_area("Input Text", height=150)

# Language Selection Dropdown
languages = {
    'English': 'en',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Italian': 'it',
    'Chinese': 'zh',
    'Japanese': 'ja',
    'Hindi': 'hi',
    'Odia': 'or'
}

selected_language = st.selectbox("Select the target language:", list(languages.keys()))

# Translate Button
if st.button("Translate"):
    if input_text:
        # Perform Translation
        translator = GoogleTranslator(source='auto', target=languages[selected_language])
        translated_text = translator.translate(input_text)
        
        # Output Translated Text
        st.subheader("Translated Text:")
        st.write(translated_text)
    else:
        st.error("Please enter some text to translate.")
