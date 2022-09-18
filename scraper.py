from selenium.webdriver.chrome.options import Options
from typing import TypedDict
from instadriver import InstaDriver
import json
import sys

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

    # Read config
    USERNAME: str = sys.argv[1]
    PASSWORD: str = sys.argv[2]
    PROFILE: str = sys.argv[3]
    PATH : str = "./chromedriver"

    # Opening Instagram
    chrome_options: Options = Options()
    chrome_options.add_argument("--headless")

    #driver : InstaDriver = InstaDriver(PATH, options=chrome_options)
    driver : InstaDriver = InstaDriver(PATH)

    driver.login(USERNAME, PASSWORD)

    # Get profile info
    profile : InstaProfile = driver.get_profile_info(PROFILE)
    print("getting profile info...")
    with open("{}.json".format(PROFILE), "w") as f:
        json.dump(profile, f, indent=4)
    print("done")
    
    # Closing Instagram
    driver.close()


