from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "Your Email ID"
ACCOUNT_PASSWORD = "your password"
PHONE = "9876543210"

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def login_to_linkedin():
    driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()

    time.sleep(5)

    email = driver.find_element(By.NAME, "session_key")
    email.send_keys(ACCOUNT_EMAIL)

    password = driver.find_element(By.NAME, "session_password")
    password.send_keys(ACCOUNT_PASSWORD)
    password.send_keys(Keys.ENTER)

def apply_to_job(job_listing):
    job_listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CSS_SELECTOR, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            return False
        else:
            submit_button.click()
            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            return True
    except NoSuchElementException:
        print("No application button, skipped.")
        return False

def main():
    login_to_linkedin()

    all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

    for idx, listing in enumerate(all_listings, start=1):
        job_info = {
            "title": listing.find_element(By.CSS_SELECTOR, ".job-card-list__title").text,
            "company": listing.find_element(By.CSS_SELECTOR, ".job-card-container__company-name").text,
            "location": listing.find_element(By.CSS_SELECTOR, ".job-card-container__metadata").text,
            "applied": apply_to_job(listing)
        }
        print(f"Job {idx}: {job_info['title']} at {job_info['company']} in {job_info['location']}")
        print("Applied" if job_info['applied'] else "Not applied")
        print("---------------")

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
