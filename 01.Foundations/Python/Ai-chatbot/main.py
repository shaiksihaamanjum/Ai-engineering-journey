from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os
import time


# ============================================================
# 1. LOAD API KEY
# ============================================================

load_dotenv()

api_key = os.getenv("my_api_key")

if not api_key:
    raise ValueError(
        "API key not found. Check your .env file."
    )

client = genai.Client(api_key=api_key)


# ============================================================
# 2. PYDANTIC MODEL
# ============================================================

class ChatResponse(BaseModel):

    answer: str = Field(
        description="The main answer to the user's question"
    )

    key_points: list[str] = Field(
        description="Important points from the answer"
    )

    sentiment: str = Field(
        description="Overall sentiment of the response"
    )


# ============================================================
# 3. STRUCTURED OUTPUT FORMAT
# ============================================================

response_format = {
    "type": "text",
    "mime_type": "application/json",
    "schema": ChatResponse.model_json_schema()
}


# ============================================================
# 4. MEMORY
# ============================================================

previous_id = None


# ============================================================
# 5. CHAT FUNCTION
# ============================================================

def chat(user_msg):

    global previous_id

    max_retries = 3

    for attempt in range(max_retries):

        try:

            # -----------------------------------------
            # First interaction
            # -----------------------------------------

            if previous_id is None:

                interaction = client.interactions.create(
                    model="gemini-3.7-flash",
                    input=user_msg,
                    response_format=response_format
                )

            # -----------------------------------------
            # Follow-up interaction
            # -----------------------------------------

            else:

                interaction = client.interactions.create(
                    model="gemini-3.7-flash",
                    input=user_msg,
                    previous_interaction_id=previous_id,
                    response_format=response_format
                )

            # -----------------------------------------
            # Save memory
            # -----------------------------------------

            previous_id = interaction.id

            # -----------------------------------------
            # JSON → Pydantic
            # -----------------------------------------

            result = ChatResponse.model_validate_json(
                interaction.output_text
            )

            return result


        # -----------------------------------------
        # Rate limit handling
        # -----------------------------------------

        except Exception as e:

            error_message = str(e)

            if (
                "429" in error_message
                or "quota" in error_message.lower()
            ):

                if attempt < max_retries - 1:

                    wait_time = 30 * (attempt + 1)

                    print(
                        f"\nRate limit reached."
                        f"\nRetrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:

                    print(
                        "\nAPI quota/rate limit exceeded."
                    )

                    return None

            else:

                raise e


# ============================================================
# 6. CHAT LOOP
# ============================================================

print("======================================")
print("       GEMINI AI CHATBOT")
print("======================================")

print("Type 'exit' to stop the chatbot.\n")


while True:

    user_msg = input("You: ")

    if user_msg.lower() == "exit":

        print("\nGoodbye!")

        break


    result = chat(user_msg)


    if result is None:

        continue


    print("\nAI:")
    print(result.answer)

    print("\nKey Points:")

    for point in result.key_points:

        print("-", point)

    print("\nSentiment:")
    print(result.sentiment)

    print("\n" + "-" * 50)
