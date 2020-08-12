import random
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from models import Account


def yahoo():
    accounts = open("Names.txt", "r")
    numbers = open("Numbers.txt", "r")
    number = numbers.readline()
    counter = 1

    while True:
        try:
            if counter == 5:
                number = numbers.readline()
                counter = 0
            line = accounts.readline().split()
            if line is None:
                break

            driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")

            driver.get('https://login.yahoo.com/account/create?specId=yidReg')
            account = Account(line[0], line[1], number)

            time.sleep(random.uniform(1.0, 10.0))
            driver.find_element_by_name("firstName").send_keys(account.firstName)

            time.sleep(random.uniform(1.0, 10.0))
            driver.find_element_by_name("lastName").send_keys(account.lastName)

            time.sleep(random.uniform(1.0, 10.0))
            driver.find_element_by_name("yid").send_keys(account.email)

            time.sleep(random.uniform(1.0, 10.0))
            driver.find_element_by_id("usernamereg-password").send_keys(account.password)

            Select(driver.find_element_by_name("shortCountryCode")).select_by_value("MA")
            driver.find_element_by_name("phone").send_keys(account.phoneNumber)

            time.sleep(random.uniform(1.0, 10.0))
            Select(driver.find_element_by_name("mm")).select_by_value(account.birthDate.month)
            driver.find_element_by_name("dd").send_keys(account.birthDate.day)
            driver.find_element_by_name("yyyy").send_keys(account.birthDate.year)

            # refill password field
            time.sleep(random.uniform(1.0, 10.0))
            driver.find_element_by_id("usernamereg-password").send_keys(account.password)

            time.sleep(random.uniform(1.0, 10.0))
            driver.find_element_by_id("reg-submit-button").click()

            input("Click after resolve Captcha and phone verification ...")

            with open('./YahooAccounts.txt', "a+") as myfile:
                bd = vars(account.birthDate)
                account.birthDate = bd

                myfile.write(str(vars(account)) + '\n')
                myfile.close()

            counter += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    yahoo()
    input("Exit")
