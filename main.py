import requests
import json
import pyttsx3

url = "http://official-joke-api.appspot.com/random_ten"
r = requests.get(url)
print("Status: " + str(r.status_code))
jsonData = json.loads(r.text)


class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup: {self.setup}\npunchline: {self.punchline}"


jokes = []

for j in jsonData:
    setup = j['setup']
    punchline = j['punchline']
    joke = Joke(setup, punchline)
    jokes.append(joke)

for joke in jokes:
    print(joke)
    print()
    pyttsx3.speak(joke.setup)
    pyttsx3.speak(joke.punchline)
