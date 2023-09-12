from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"

name = os.getenv("NAME")
password = os.getenv("PASSWORD")

if name is None:
    name = input("Enter your username: ")

if password is None:
    name = input("Enter your password: ")

# browser set up
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(URL)

print("Navigation débutée...")

driver.find_element(
    By.CLASS_NAME, 'form__label').click()
redirect = driver.find_element(By.ID, 'button-submit')
redirect.click()

time.sleep(0.5)

print("Redirection vers la section élèves...")

pupil_section_button = driver.find_element(By.ID, 'bouton_eleve')
pupil_section_button.click()

time.sleep(0.5)

print("Saisie des infos...")

# Find the input field by its HTML attribute (e.g., name or ID)
username_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
submit_button = driver.find_element(By.ID, 'bouton_valider')


# Fill out the form fields
username_input.send_keys(name)
password_input.send_keys(password)
time.sleep(0.75)

# Submit the form (assuming the submit button has a type="submit" attribute)
submit_button.send_keys(Keys.RETURN)

print("Vous êtes maintenant connecté !")
