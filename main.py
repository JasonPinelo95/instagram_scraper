from typing import TypedDict
from instadriver import InstaDriver
import json
import time


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
    driver : InstaDriver = InstaDriver(PATH)
    driver.login(USERNAME, PASSWORD)

    # Get profile info
    #PROFILE = "jmbalanzar"
    PROFILE = "valter_med"

    profile : InstaProfile = driver.get_profile_info(PROFILE)
    print(profile)
    
    # Closing Instagram
    time.sleep(5)
    driver.close()


