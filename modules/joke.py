import requests
joke_apis = "https://v2.jokeapi.dev/joke/Programming,Pun"

# gets json datas from joke_apis

def joke_api():
    response = requests.get(joke_apis).json()
    try:
        if response["type"] == "single":
            try:
                joke = response["joke"]
            except BaseException:
                joke = response["value"]["joke"]
        elif response["type"] == "twopart":
            try:
                joke = response["setup"] + "\n\n" + response["delivery"]
            except BaseException:
                joke = response["setup"] + "\n\n" + response["punchline"]
    except BaseException:
        joke = response["type"]

    return str(joke)
#print(joke_api())

