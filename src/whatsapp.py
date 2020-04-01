from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker

faker = Faker()
options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
options.add_argument(
    r"user-data-dir=C:\Users\**\AppData\Local\Google\Chrome\User Data\Default")

driver = webdriver.Chrome(options=options)
chatlist_search = "#side > div.rRAIq > div > label > div > div._2S1VP.copyable-text.selectable-text"

chat_box = "#main > footer > div._3pkkz.V42si.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text"

participant_search = "#app > div > div > div.YD4Yw > div._1-iDe._1xXdX > span > div > span > div > div > div._66JgU > div > div > input"

configurationSubmit = "#app > div > div > div.YD4Yw > div._1-iDe._1xXdX > span > div > span > div > div > span > div"

groupNameBox = "#app > div > div > div.YD4Yw > div._1-iDe._1xXdX > span > div > span > div > div > div:nth-child(2) > div > div._1DTd4 > div > div._2S1VP.copyable-text.selectable-text"

createGroupSubmit = "#app > div > div > div.YD4Yw > div._1-iDe._1xXdX > span > div > span > div > div > span > div > div"

exitMenuBtn = "#main > header > div.YmSrp > div > div:nth-child(3) > div"

exitbtn =  "#app > div > span:nth-child(2) > div > div > div > div > div > div > div._3QNwO > div._1WZqU.PNlAR"
driver.get("https://web.whatsapp.com")
assert "WhatsApp" in driver.title


def spamTarget(targetName, message):
    trgt = '//span[@title="{}"]'.format(targetName)
    search = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, chatlist_search))
    )
    search.send_keys(targetName)

    target = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, trgt))
    )
    target.click()

    chat = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, chat_box))
    )
    for i in range(5):
        chat.send_keys(message)
        chat.send_keys(Keys.RETURN)

def createGroup(targetList):
    menu_button = '//div[@title="Menu"]'
    newGroupBtn = '//div[@title="New group"]'
    exitGroupBtn = "#main > header > div.YmSrp > div > div.rAUz7._3TbsN > span > div > ul > li:nth-child(5) > div"

    menu = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, menu_button))
        )
    menu.click()

    newGroup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, newGroupBtn))
        )
    newGroup.click()
    
    for targetName in targetList:
        trgt = '//span[@title="{}"]'.format(targetName)

        participant_find = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, participant_search))
        )
        participant_find.send_keys(targetName)


        target = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, trgt))
        )
        target.click()

    configurationGroup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, configurationSubmit))
        )
    configurationGroup.click()

    groupName = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, groupNameBox))
        )
    groupName.send_keys(faker.company())

    createGroup = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, createGroupSubmit))
        )
    createGroup.click()
    time.sleep(1)
    # exitmenu = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, exitMenuBtn))
    #     )
    # exitmenu.click()

    
    # exitGroup = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, exitGroupBtn))
    #     )
    # exitGroup.click()

    # findexitbtn = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, exitbtn))
    #     )
    # findexitbtn.click()

for i in range(50):
    createGroup(["username"])

# try:
# finally:
#     time.sleep(20)
#     driver.quit()
