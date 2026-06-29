from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

EMAIL = "akkalkotshristhi@gmail.com"
PASSWORD = "Food@1985"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://vtu.internyet.in/")

time.sleep(3)

# Find fields
username_box = driver.find_element(By.NAME, "email")
password_box = driver.find_element(By.NAME, "password")

# Enter credentials
username_box.send_keys(EMAIL)
password_box.send_keys(PASSWORD)

# Login button
login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

time.sleep(5)

# Open diary page
driver.get("https://vtu.internyet.in/dashboard/student/diary-entries")

time.sleep(5)

# Count rows
rows = driver.find_elements(By.TAG_NAME, "tr")

print("\nTotal Diary Entries:", len(rows) - 1)

# Optional: print all entries
for row in rows[1:]:
    print(row.text)

input("\nPress Enter to close...")
driver.quit()