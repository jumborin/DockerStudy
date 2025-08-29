from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_gitlab_access():
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )
    
    try:
        driver.get('http://gitlab:8081')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("GitLab access test: PASSED")
    except Exception as e:
        print(f"GitLab access test: FAILED - {e}")
    finally:
        driver.quit()

def test_jenkins_access():
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )
    
    try:
        driver.get('http://jenkins:8080')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Jenkins access test: PASSED")
    except Exception as e:
        print(f"Jenkins access test: FAILED - {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Starting CI/CD environment tests...")
    test_gitlab_access()
    test_jenkins_access()
    print("Tests completed.")