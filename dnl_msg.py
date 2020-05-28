"""
Przykład na zajęcia z WWW
Filmik na kanale
"""

import argparse
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pobierz(login, haslo):
    """
    pobierz('123', 'has')
    """
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get('https://portal.librus.pl/rodzina/synergia/loguj')
    element = driver.find_element_by_link_text("LIBRUS Synergia")
    element.click()
    element = driver.find_element_by_xpath("//a[contains(@href, '/rodzina/synergia/loguj')]")
    element.click()
    driver.switch_to.frame(0)
    element = driver.find_element_by_id("Login")
    element.send_keys(login)
    element = driver.find_element_by_id("Pass")
    element.send_keys(haslo)
    element = driver.find_element_by_id("LoginBtn")
    element.click()
    time.sleep(2)
    driver.switch_to.default_content()
    element = driver.find_element_by_xpath("//a[@id='icon-wiadomosci']/span")
    element.click()
    elements = driver.find_elements_by_css_selector(".line0, .line1")
    for element in elements:
        print(element.text)
    driver.quit()

def main():
    """
    no main a co?
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("login")
    parser.add_argument("haslo")
    args = parser.parse_args()
    pobierz(args.login, args.haslo)

if __name__ == '__main__':
    main()
