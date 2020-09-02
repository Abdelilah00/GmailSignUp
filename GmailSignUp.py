import random
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from models import Account


def gmail():
    accounts = open("Names.txt", "r")
    global driver

    while True:
        try:
            """if counter == 5:
                number = numbers.readline()
                counter = 0"""

            line = accounts.readline().split()
            if line is None:
                break

            # proxy = FreeProxy(rand=True).get()
            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--proxy-server=%s' % proxy)
            # chrome_options.add_argument("user-data-dir=C:\Users\Alexis\AppData\Local\Google\Chrome\User Data\Default")
            driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")

            driver.get(
                'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
            account = Account(line[0], line[1])

            action = webdriver.ActionChains(driver)
            
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/button")
            elem.click()
            time.sleep(random.uniform(1.0, 5.5))

            elem = driver.find_element_by_name("firstName")
            action.move_to_element(elem).perform()
            elem.send_keys(account.firstName)
            time.sleep(random.uniform(1.0, 5.5))

            elem = driver.find_element_by_name("lastName")
            action.move_to_element(elem).perform()
            elem.send_keys(account.lastName)
            time.sleep(random.uniform(1.0, 5.5))

            elem = driver.find_element_by_name("Username")
            action.move_to_element(elem).perform()
            elem.send_keys(account.email)
            time.sleep(random.uniform(1.0, 5.5))

            elem = driver.find_element_by_name("Passwd")
            action.move_to_element(elem).perform()
            elem.send_keys(account.password)
            time.sleep(random.uniform(1.0, 5.5))

            elem = driver.find_element_by_name("ConfirmPasswd")
            action.move_to_element(elem).perform()
            elem.send_keys(account.password)
            time.sleep(random.uniform(1.0, 5.5))

            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/span/span").click()
            time.sleep(random.uniform(1.0, 5.5))

            ############################################
            driver.find_element_by_id("day").send_keys(account.birthDate.day)
            time.sleep(random.uniform(1.0, 5.5))
            Select(driver.find_element_by_id("month")).select_by_value(account.birthDate.month)
            time.sleep(random.uniform(1.0, 5.5))
            driver.find_element_by_id("year").send_keys(account.birthDate.year)
            Select(driver.find_element_by_id('gender')).select_by_value(str(random.randint(1, 2)))

            ############################################

            input("new gmail")

            with open('./GmailAccounts.txt', "a+") as myfile:
                bd = vars(account.birthDate)
                account.birthDate = bd

                myfile.write(str(vars(account)) + '\n')
                myfile.close()

            # counter += 1
        except Exception as e:
            print(e)
        finally:
            driver.quit()


if __name__ == "__main__":
    gmail()
    input("Exit")
