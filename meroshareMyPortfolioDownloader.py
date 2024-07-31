from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

# Define your credentials
username = 'yourMeroshareID'
password = 'yourPassword'

# Set up the Edge options
options = webdriver.EdgeOptions()
prefs = {"download.default_directory": "D:\Study\Data analyst\Share market portfolio\meroshareMyPortfolio"}
options.add_experimental_option("prefs", prefs)

# Add custom user-agent to mimic a real browser
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

# Initialize the WebDriver
driver = webdriver.Edge(options=options)

# Maximize the browser window to make it fullscreen
#driver.maximize_window()

try:
    # Step 1: Go to the Mero Share login page
    driver.get('https://meroshare.cdsc.com.np/')

    # Introduce a delay to ensure the page loads completely
    time.sleep(2)
    
    # Step 2: Click the dropdown button to open it
    dp_dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "selectBranch"))
    )
    dp_dropdown_button.click()

    # Introduce a delay to ensure the dropdown options load
    time.sleep(2)

    # Step 3: Select the desired option by clicking it
    desired_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'NIC ASIA BANK LIMITED (13700)')]"))
    )
    desired_option.click()

    # Step 3: Enter the username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys(username)
    
    # Trigger input event after entering the username
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'))", username_input)

    # Step 4: Enter the password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)

     # Trigger input event after entering the password
    driver.execute_script("arguments[0].dispatchEvent(new Event('input'))", password_input)

    # Introduce a delay to mimic human behavior
    time.sleep(2)
    
    # Step 5: Click the login button directly
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Wait for the login to complete
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "user-control-header"))
    )


    # Introduce a delay to ensure the page loads completely
    time.sleep(3)
    
    # Step 6: Navigate to the portfolio page
    driver.get('https://meroshare.cdsc.com.np/#/portfolio')

    # Introduce a delay to ensure the page loads completely
    time.sleep(3)
    
    # Step 7: Click the CSV download button
    csv_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-outline' and contains(., 'CSV')]"))
    )
    csv_button.click()
    
    print("CSV download initiated!")

    time.sleep(3)

    


except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()

