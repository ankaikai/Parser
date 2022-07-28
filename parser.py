from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.facebook.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

username.clear()
username.send_keys("YOUR_EMAIL")
password.clear()
password.send_keys("YOUR_PASS")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)

driver.get("https://www.facebook.com/profile.php?id=100080484246024")

time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

elements_posts = driver.find_elements(By.CSS_SELECTOR, "div.rq0escxv.l9j0dhe7.du4w35lb.hpfvmrgz.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.gile2uim.pwa15fzy.fhuww2h9")
for el in elements_posts:
    parsed_words = el.text

#path to arrays with words and sites#
path_to_bad_words = './bad_words.txt'
path_to_dangerous_sites = './Informational_dangerous_sites.txt'

#extract data from txt
def extract_data(path):
    data_read = ""
    file = open(path, encoding='utf-8')
    for line in file:
        data_read += line.lower()
    return data_read

#extract list of words and sites
bad_words_text = extract_data("./bad_words.txt")
informational_dang_sites = extract_data("./Informational_dangerous_sites.txt")
bad_words = bad_words_text.split("\n")
dang_sites = informational_dang_sites.split("\n")

#checking of bad words equals
countBadWords = 0
for bad_word in bad_words:
    if bad_word in parsed_words:
        countBadWords += 1

#checking of danger sites equals
countBadSites = 0
for bad_site in dang_sites:
    if bad_site in parsed_words:
        countBadSites += 1

#result of program
print("          Результат:")
print(f"Кількість використаних нецензурних слів: {countBadWords}")
if countBadWords >= 5:
    print("Вживає нецензурну лексику")

print(f"Кількість маніпулятнивних сайтів на сторінці: {countBadSites}")
if countBadSites >= 3:
    print("Піддається маніпуляції")