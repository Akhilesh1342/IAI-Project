import streamlit as st
from openai import OpenAI
client = OpenAI(
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

# Streamlit UI
st.set_page_config(page_title="AI Study Assistant")

st.title("📚 AI Study Assistant")
st.write("Ask me anything about studies, programming, or AI!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask a question...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=st.session_state.messages
    )

    ai_response = response.choices[0].message.content

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)