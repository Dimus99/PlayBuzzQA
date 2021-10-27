from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ChoiceType import ChoiceType


class PlayBuzzManager:
    count_questions = 9

    def __init__(self, url, test_name, wait_page_timeout=130, executable_path="./geckodriver"):
        self.test_name = test_name
        self.wait_page_timeout = wait_page_timeout
        try:
            self.driver = webdriver.Firefox()
        except:
            self.driver = webdriver.Firefox(executable_path=executable_path)
        self.driver.implicitly_wait(wait_page_timeout)
        self.driver.get(url)
        self._start_test()

    def _start_test(self):
        self.driver.find_element(By.CLASS_NAME, "intro-start-btn").click()

    def make_choices(self, choices: List[ChoiceType]):
        driver = self.driver
        for question_number in range(self.count_questions):
            self.wait_page(
                lambda window: window.find_element(
                    By.CLASS_NAME, "pb-quiz-question-progress").find_element(
                    By.TAG_NAME, "b").text == str(question_number + 1))
            driver.find_elements(by=By.CLASS_NAME, value="image-border")[
                choices[question_number].value].click()

        return self._get_result()

    def _get_result(self):
        driver = self.driver
        self.wait_page(
            lambda window: window.find_element(
                By.CLASS_NAME, "result-title").find_element(
                By.CLASS_NAME, "text-viewer-component").find_element(
                By.TAG_NAME, "p").text)
        result_title = driver.find_element(
            By.CLASS_NAME, "result-title").find_element(
            By.CLASS_NAME, "text-viewer-component").find_element(
            By.TAG_NAME, "p").text
        result_body = driver.find_element(
            By.CLASS_NAME, "result-desc").find_element(
            By.CLASS_NAME, "text-viewer-component").find_element(
            By.TAG_NAME, "p").text
        return Result(result_title, result_body)

    def save_screenshot(self, path="screenshots/"):
        self.driver.save_screenshot(path + self.test_name + ".png")

    def wait_page(self, condition):
        WebDriverWait(self.driver, self.wait_page_timeout).until(condition)

    def quit(self):
        self.driver.close()
        self.driver.quit()


class Result:
    def __init__(self, title, body):
        self.title = title
        self.body = body
