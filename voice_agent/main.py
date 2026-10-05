import asyncio
from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
import os
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
async_client = AsyncOpenAI()


async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=speech,
        instructions="Speak in a cheerful and positive tone.",
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)


def main():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 2
            print("Listening... Speak now.")

            audio = recognizer.listen(source)

            print("Processing Audio : STT...")
            stt = recognizer.recognize_google(audio)

            print("You said:", stt)

            SYSTEM_PROMPT = """
                You're an expert voice agent. You are given an transcript of what user has said using voice.
                You need to output as if you are an voice agent and whatever you speak will be converted back to audio using ai and played back to user
            """

            response = openai_client.chat.completions.create(
                model="gemini-3.5-flash-lite",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": stt},
                ],
            )

            print("AI Response:", response.choices[0].message.content)

            asyncio.run(tts(speech=response.choices[0].message.content))

    except sr.WaitTimeoutError:
        print("No speech detected within the timeout period.")
        return None
    except OSError:
        print("Microphone not found or not accessible.")
        return None


main()
