from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Selenium GridのHub URL
#hub_url = "http://localhost:4444/wd/hub" #Dockerコンテナ外で実行する場合
hub_url = "http://selenium-hub:4444/wd/hub" #Dockerコンテナ内で実行する場合

# Chrome用のオプションを設定
chrome_options = Options()

# Chromeでのテスト
chrome_driver = webdriver.Remote(
    command_executor=hub_url,
    options=chrome_options 
)

# テスト処理開始
chrome_driver.get("https://www.google.com")
print(chrome_driver.title)

# スクリーンショット保存
screenshot_path = "../screenshot/google.png"
chrome_driver.save_screenshot(screenshot_path)
print(f"スクリーンショットを保存しました: {screenshot_path}")

#Redmine
chrome_driver.get("https://www.redmine.org/projects/redmine/wiki/RedmineInstall")
print(chrome_driver.title)
screenshot_path = "../screenshot/RedmineInstall.png"
chrome_driver.save_screenshot(screenshot_path)
print(f"スクリーンショットを保存しました: {screenshot_path}")

# 終了処理
chrome_driver.quit()


