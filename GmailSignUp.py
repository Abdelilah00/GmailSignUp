import os
import time
from fp.fp import FreeProxy
from selenium import webdriver
from selenium.webdriver.support.select import Select

from models import Account, BirthDate


def gmail():
    accounts = open("Names.txt", "r")
    numbers = open("Numbers.txt", "r")
    number = numbers.readline()
    counter = 0
    changeNumber = False

    while True:
        try:
            if changeNumber:
                number = numbers.readline()
            line = accounts.readline().split()
            if line is None:
                break

            proxy = FreeProxy(rand=True).get()

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % proxy)
            driver = webdriver.Chrome(options=chrome_options, executable_path="D:\\chromedriver.exe")

            driver.get(
                'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

            account = Account(line[0], line[1], line[0] + line[1] + "1234567890", "XY1234567890YX",
                              BirthDate())

            driver.find_element_by_name("firstName").send_keys(account.firstName)
            driver.find_element_by_name("lastName").send_keys(account.lastName)
            driver.find_element_by_name("Username").send_keys(account.email)
            driver.find_element_by_name("Passwd").send_keys(account.password)
            driver.find_element_by_name("ConfirmPasswd").send_keys(account.password)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span").click()
            time.sleep(5)

        

            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input").send_keys(
                number)
            input("continue")

            driver.find_element_by_id("day").send_keys(account.birthDate.day)
            Select(driver.find_element_by_id("month")).select_by_value(account.birthDate.month)
            driver.find_element_by_id("year").send_keys(account.birthDate.year)
            Select(driver.find_element_by_id('gender')).select_by_value('2')
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[2]").click()
            time.sleep(5)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div/div/div[2]/div/div[1]/div/span/span").click()
            time.sleep(5)

            with open('./GmailAccounts.txt', "a+") as myfile:
                bd = vars(account.birthDate)
                account.birthDate = bd

                myfile.write(str(vars(account)) + '\n')
                myfile.close()

            input("new gmail")

            counter += 1
            if counter == 5:
                counter = 0
                changeNumber = True
            else:
                changeNumber = False

        except Exception as e:

            print(e)


if __name__ == "__main__":
    gmail()
    input("Exit")
