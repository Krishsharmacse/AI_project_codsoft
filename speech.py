import speech_recognition as sr
import pyttsx3
import pyjokes
import webbrowser
import re
import sympy as sp

recognizer = sr.Recognizer()
engine = pyttsx3.init()
#List all available voices
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


# property for speed of voice
engine.getProperty('rate')
engine.setProperty('rate',150)

# Function to speak text using pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()
def format_math_expression(expression):
    # Replace 'x' with '*' for multiplication
    expression = expression.replace('x', '*')
    # Remove any extra spaces
    expression = expression.replace(' ', '')
    return expression
def solve_math_expression(expression):
    try:
        # Format the expression for better parsing
        expression = format_math_expression(expression)
        
        # Try evaluating using eval() for basic calculations
        result = eval(expression)
    except Exception:
        # If eval fails, try using SymPy for more complex expressions
        expr = sp.sympify(expression)
        result = sp.simplify(expr)
    return result



# Function to listen and recognize speech
def listen_and_recognize():
    try:
        with sr.Microphone() as mic:
            # Speak before starting to recognize
            speak("I am listening")
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            print("Listening...")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")
    
            # If the recognized text includes 'tell me a joke', tell a joke
            math_pattern = r"[-+]?\d+(\.\d+)?([/*+-]\d+(\.\d+)?)*"
            if re.match(math_pattern, text):
                speak("Solving the math problem.")
                result = solve_math_expression(text)
                print(f"Math result: {result}")
                speak(f"The result is {result}")
            elif "tell me a joke" in text:
                joke = pyjokes.get_joke()
                print(f"Joke: {joke}")
                speak(joke)
              # If the recognized text is 'play google assistant song', open YouTube link
            elif "sing a song" in text:
                speak("Playing Google Assistant song")
                speak('''I am your personal Assistant TUTUTU tututu i am here to help you i can work for you play for ypu dance for you  ''')
            elif "open youtube" in text:
                speak("opening youtube...")
                webbrowser.open("https://www.youtube.com")
            elif "open linkedin" in text:
                speak("opening linkedin...")
                webbrowser.open("https://www.linkedin.com/in/krish-sharma-212325282/")
            elif "open google" in text:
                speak("opening Google...")
                webbrowser.open("https://www.google.com/url")
            elif "question" in text:
                speak("opening Chat Gpt")
                webbrowser.open("https://chatgpt.com/")
            elif "what can you do" in text:
                speak(" i can do anything that an normal ai can work ")
            else:
                # Speak the recognized text back to the user
                speak(f"You said: {text} i am working on it")
            
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        speak("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("There was a problem connecting to the speech service.")

def listen_for_wake_word():
    try:
        with sr.Microphone() as mic:
            print("Litening Please Wake Me...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = recognizer.listen(mic)
            word = recognizer.recognize_google(audio).lower()

            if "jarvis" in word:
                speak("Yes sir initializing Jarvis?")
                print("Initializing Jarvis...")
                listen_and_recognize()  # Call the main recognition function
    

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        speak("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("There was a problem connecting to the speech service.")



if __name__ == "__main__":
    while True:
        listen_for_wake_word()  # Continuously listen for the wake word
