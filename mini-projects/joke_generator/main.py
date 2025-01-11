import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Couldn't fetch a joke at the moment. Please try again later."

if __name__ == "__main__":
    joke = get_joke()
    print("Here's a random joke for you:")
    print(joke)
