from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstaDriver(webdriver.Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.maximize_window()

    def login(self, username: str, password: str):
        """Login to Instagram"""
        self.get("https://www.instagram.com/")
        self.implicitly_wait(5)
        self.find_element(By.NAME, "username").send_keys(username)
        self.find_element(By.NAME, "password").send_keys(password)
        self.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.implicitly_wait(5)
        self.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        self.implicitly_wait(5)
        self.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

    def __get_profile(self, username: str):
        """Get profile page"""
        self.get(f"https://www.instagram.com/{username}/")
        self.implicitly_wait(5)
    
    def __get_biography(self, username: str):
        """Get biography"""
        return self.find_element(By.CSS_SELECTOR, "._aa_c").text
    
    def __get_num_posts(self, username: str):
        """Get number of posts"""
        return int(self.find_element(By.CSS_SELECTOR, "ul li:nth-of-type(1) span").text.replace(",", ""))
    
    def __get_follower_count(self, username: str):
        """Get follower count"""
        return int(self.find_element(By.CSS_SELECTOR, "ul li:nth-of-type(2) span").text.replace(",", ""))
    
    def __get_following_count(self, username: str):
        """Get following count"""
        return int(self.find_element(By.CSS_SELECTOR, "ul li:nth-of-type(3) span").text.replace(",", ""))

    def __get_is_private(self, username: str):
        """Get is private"""
        return len(self.find_elements(By.CSS_SELECTOR, "div h2")) > 1

    def __get_post_info(self, post):
        """Get post info"""
        return {
            "username": post.find_element(By.CSS_SELECTOR, "a").get_attribute("title"),
            "post_url": post.find_element(By.CSS_SELECTOR, "a").get_attribute("href"),
            "img_url": post.find_element(By.CSS_SELECTOR, "img").get_attribute("src"),
            "caption": post.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) span").text
        }        
    
    def get_profile_info(self, username: str):
        """Get profile info"""
        self.__get_profile(username)
        return {
            "username": username,
            "biography": self.__get_biography(username),
            "num_posts": self.__get_num_posts(username),
            "follower_count": self.__get_follower_count(username),
            "following_count": self.__get_following_count(username),
            "is_private": self.__get_is_private(username)
        }



