import browser_cookie3
from Bard import Chatbot
from decouple import config


def get_chatbot():
    BARD_SESSION = config('BARD_SESSION', default="")
    if BARD_SESSION == "":
        print("BARD_SESSION not found on env file, trying to retrieve it from chrome")
        cookies = browser_cookie3.chrome(domain_name="google.com")

        for cookie in cookies:
            if cookie.name == '__Secure-1PSID':
                BARD_SESSION = cookie.value
                break

    if BARD_SESSION:
        chatbot = Chatbot(BARD_SESSION)
        return chatbot
    else:
        raise ValueError(
            "Session key is not found, add your bard session on .env file in root folder or login to https://bard.google.com/ from chrome(not in incognito mode) and try again "
        )


if __name__ == "__main__":
    chatbot = get_chatbot()
    response = chatbot.ask("Hi there")
    print(response)
