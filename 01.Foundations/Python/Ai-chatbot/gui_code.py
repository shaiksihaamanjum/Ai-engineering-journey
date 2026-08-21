import streamlit as st
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
import time


# ============================================================
# 1. PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ============================================================
# 2. LOAD API KEY
# ============================================================

load_dotenv()

api_key = os.getenv("my_api_key")

if not api_key:

    st.error(
        "API key not found. Check your .env file."
    )

    st.stop()


client = genai.Client(api_key=api_key)


# ============================================================
# 3. PYDANTIC MODEL
# ============================================================

class ChatResponse(BaseModel):

    answer: str = Field(
        description="The main answer to the user's message"
    )

    key_points: list[str] = Field(
        description="Important points from the answer"
    )

    sentiment: str = Field(
        description="Overall sentiment of the response"
    )


# ============================================================
# 4. STRUCTURED OUTPUT
# ============================================================

response_format = {
    "type": "text",
    "mime_type": "application/json",
    "schema": ChatResponse.model_json_schema()
}


# ============================================================
# 5. SESSION STATE
# ============================================================

if "previous_id" not in st.session_state:

    st.session_state.previous_id = None


if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# 6. CHAT FUNCTION
# ============================================================

def chat(user_msg):

    max_retries = 3

    for attempt in range(max_retries):

        try:

            # -----------------------------------------
            # First message
            # -----------------------------------------

            if st.session_state.previous_id is None:

                interaction = client.interactions.create(
                    model="gemini-3.7-flash",
                    input=user_msg,
                    response_format=response_format
                )

            # -----------------------------------------
            # Continue conversation
            # -----------------------------------------

            else:

                interaction = client.interactions.create(
                    model="gemini-3.7-flash",
                    input=user_msg,
                    previous_interaction_id=(
                        st.session_state.previous_id
                    ),
                    response_format=response_format
                )


            # -----------------------------------------
            # Save interaction ID
            # -----------------------------------------

            st.session_state.previous_id = interaction.id


            # -----------------------------------------
            # JSON → Pydantic
            # -----------------------------------------

            result = ChatResponse.model_validate_json(
                interaction.output_text
            )


            return result


        # -----------------------------------------
        # 429 handling
        # -----------------------------------------

        except Exception as e:

            error_message = str(e)

            if (
                "429" in error_message
                or "quota" in error_message.lower()
            ):

                if attempt < max_retries - 1:

                    wait_time = 30 * (attempt + 1)

                    time.sleep(wait_time)

                else:

                    st.error(
                        "Gemini API quota/rate limit exceeded."
                    )

                    return None

            else:

                st.error(
                    f"API Error: {e}"
                )

                return None


# ============================================================
# 7. TITLE
# ============================================================

st.title("🤖 AI Chatbot")

st.caption(
    "Gemini + Interactions API + Pydantic + JSON + Memory"
)


# ============================================================
# 8. SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Settings")

    st.write("Memory:")

    if st.session_state.previous_id:

        st.success("ON")

    else:

        st.info("New conversation")


    st.divider()


    if st.button("🗑️ New Conversation"):

        st.session_state.previous_id = None

        st.session_state.messages = []

        st.rerun()


# ============================================================
# 9. DISPLAY OLD MESSAGES
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["answer"])

        if message["role"] == "assistant":

            if message.get("key_points"):

                st.write("**Key Points:**")

                for point in message["key_points"]:

                    st.write("•", point)

            if message.get("sentiment"):

                st.caption(
                    f"Sentiment: {message['sentiment']}"
                )


# ============================================================
# 10. USER INPUT
# ============================================================

user_msg = st.chat_input(
    "Ask me anything..."
)


if user_msg:

    # -----------------------------------------
    # Display user message
    # -----------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "answer": user_msg
        }
    )


    with st.chat_message("user"):

        st.write(user_msg)


    # -----------------------------------------
    # Get AI response
    # -----------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = chat(user_msg)


        if result:

            st.write(result.answer)


            st.write("**Key Points:**")

            for point in result.key_points:

                st.write("•", point)


            st.caption(
                f"Sentiment: {result.sentiment}"
            )


            # -----------------------------------------
            # Save structured response
            # -----------------------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "answer": result.answer,
                    "key_points": result.key_points,
                    "sentiment": result.sentiment
                }
            )