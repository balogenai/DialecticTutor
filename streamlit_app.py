import streamlit as st
from tutor_chain import create_tutor_chain

st.set_page_config(page_title="Dialectic Tutor", page_icon="🧠")
st.title("🧠 Dialectic Tutor")
st.subheader("Learn by Asking Questions!")

# Init session state
if "chain" not in st.session_state:
    st.session_state.chain = create_tutor_chain()
    st.session_state.chat_log = []
    st.session_state.ended = False

# Chat input
user_input = st.chat_input("Ask your tutor something...")

if user_input and not st.session_state.ended:
    with st.spinner("🤖 Tutor is thinking..."):
        response = st.session_state.chain.run(student_input=user_input)

    # Update chat history
    st.session_state.chat_log.append(("You", user_input))
    st.session_state.chat_log.append(("Tutor", response))

# Display chat history
for speaker, message in st.session_state.chat_log:
    with st.chat_message(speaker.lower() if speaker == "You" else "assistant"):
        st.markdown(message)

