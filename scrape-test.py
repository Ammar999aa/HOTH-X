from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://web.cs.ucla.edu/classes/spring22/cs31/syllabus.html")
# assert "Python" in driver.title
elem = driver.find_element(By.XPATH, "/html/body/div[1]/h2[1]")
elemt = elem.text
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()


def main():
    print("Hello")
    print(elemt)


if __name__ == "__main__":
    main()
