# scraper/youtube_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class YouTubeScraper:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    def open_video(self, video_url):
        self.driver.get(video_url)
        time.sleep(2)
    
    def scroll_to_load_comments(self):
        for _ in range(5):  # Adjust the range for more scrolling
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(2)

    def get_comments(self):
        comments = []
        usernames = []
        comment_elements = self.driver.find_elements(By.XPATH, '//*[@id="content-text"]')
        username_elements = self.driver.find_elements(By.XPATH, '//*[@id="author-text"]/span')

        for comment_element, username_element in zip(comment_elements, username_elements):
            comments.append(comment_element.text)
            usernames.append(username_element.text.strip())

        return usernames, comments

    def close_driver(self):
        self.driver.quit()
