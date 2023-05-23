import browser_cookie3
from Bard import Chatbot
from decouple import config


available_browser_functions = {
    "chrome": browser_cookie3.chrome,
    "firefox": browser_cookie3.firefox,
    "edge": browser_cookie3.edge,
    "brave": browser_cookie3.brave,
    "safari": browser_cookie3.safari,
}


def get_session_from_browser():
    print("BARD_SESSION not found on env file\n")
    SELECTED_BROWSER = config('SELECTED_BROWSER', default="").strip()
    if SELECTED_BROWSER == "":
        raise ValueError("You need to specify either BARD_SESSION or SELECTED_BROWSER in the env file")

    BARD_SESSION = ""

    browser_function = available_browser_functions.get(SELECTED_BROWSER)
    if browser_function is None:
        available_chocies = ', '.join(available_browser_functions.keys())
        raise ValueError(f"Invalid browser selected, available choices are {available_chocies}")

    print(
        f"Trying to retrieve bard session from {SELECTED_BROWSER}, this only works if you have logged into https://bard.google.com/ from {SELECTED_BROWSER} in non-incognito mode\n"
    )

    cookies = browser_function(domain_name="google.com")

    for cookie in cookies:
        if cookie.name == '__Secure-1PSID':
            if cookie.value != "":
                BARD_SESSION = cookie.value
                print("Retrieved session file\n")
                break

    return BARD_SESSION


def get_chatbot():
    BARD_SESSION = config('BARD_SESSION', default="") or get_session_from_browser()

    if BARD_SESSION:
        chatbot = Chatbot(BARD_SESSION)
        return chatbot
    else:
        raise ValueError(
            "Bard session not found, add your bard session in .env file in root folder or login to https://bard.google.com/ from a browser(not in incognito mode) and add it to your env file and try again "
        )


if __name__ == "__main__":
    chatbot = get_chatbot()
    response = chatbot.ask("Hi there")
    print(response)
