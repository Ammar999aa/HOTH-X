from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.google.com/travel/flights/search?tfs=CBwQAhoqag4IAhIKL20vMDMwcWIzdBIKMjAyMy0wMy0yMXIMCAMSCC9tLzAxM3lxGipqDAgDEggvbS8wMTN5cRIKMjAyMy0wMy0yNXIOCAISCi9tLzAzMHFiM3RwAYIBCwj___________8BQAFIAZgBAQ")
wait = WebDriverWait(driver, 200)
elem = driver.find_element(
    By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/h3')

elem2 = driver.find_element(
    By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div/div[4]/div/div/div[2]/div[1]/div/div[1]/span/button/span/span/span')
# assert "Python" in driver.title
# elem = driver.find_element(By.XPATH, "/html/body/div[1]/h2[1]")
elemt = elem.text
elemt2 = elem2.text
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()


def main():
    print("Hello")
    print(elemt)
    print(elemt2)


if __name__ == "__main__":
    main()
