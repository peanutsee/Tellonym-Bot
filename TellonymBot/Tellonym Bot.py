from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from questions import QuestionsScraper
from time import sleep

class TellonymBot():
    def __init__(self):
        # Chrome Settings
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=chrome_options)

    def askQuestions(self, url, questions):
        # Predefined Variables
        delay = 2
        wait = WebDriverWait(self.driver, delay)

        # Get URL
        self.driver.get(url)

        # Check Len of Questions
        if len(questions) > 1:
            for question in questions:
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[4]/div[3]'))).click()
                except:
                    # Text Box
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea'))).send_keys(question)
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[2]/form/button'))).click()
                    sleep(1) # Allow time for server to render requests
        else:
            # Text Box
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea'))).send_keys(questions[0])
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[2]/form/button'))).click()
        self.driver.close()

questions = QuestionsScraper().questions()
url = # INSERT ULR HERE
TellonymBot().askQuestions(url, questions)
