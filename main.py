from selenium.webdriver.chrome.options import Options
from typing import TypedDict
from instadriver import InstaDriver
import json

class Config(TypedDict):
    username : str
    password : str

class InstaProfile(TypedDict):
    username : str
    biography : str
    num_posts : int
    follower_count : int
    following_count : int
    is_private : bool

if __name__ == "__main__":
    # Read credentianls from config file

    with open("config.json") as f:
        config: Config = json.load(f)
        USERNAME: str = config["username"]
        PASSWORD: str = config["password"]

    PATH : str = "./chromedriver"

    # Opening Instagram
    chrome_options: Options = Options()
    chrome_options.add_argument("--headless")

    driver : InstaDriver = InstaDriver(PATH, options=chrome_options)
    driver.login(USERNAME, PASSWORD)

    # Get profile info
    #PROFILE = "jmbalanzar"
    PROFILE = "valter_med"

    profile : InstaProfile = driver.get_profile_info(PROFILE)
    print("getting profile info...")
    print(json.dumps(profile, indent=4))
    print("done")
    
    # Closing Instagram
    driver.close()


