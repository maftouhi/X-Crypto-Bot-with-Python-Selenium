import time
import cryptocompare
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def login(username, password):
    driver.get('https://twitter.com/i/flow/login')
    try:
        input_field_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="text"]')))
        input_field_username.send_keys(username)
        input_field_username.send_keys(Keys.RETURN)
        try:
            input_field_password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
            input_field_password.send_keys(password)
            input_field_password.send_keys(Keys.RETURN)
            time.sleep(5)
        except:
            driver.quit()
    except:
        driver.quit()


def reply():
    driver.get('https://twitter.com/notifications/mentions')
    time.sleep(5)
    for i in range(2400):  # limit set by latest Twitter update
        try:
            mentions = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
            if mentions[i] is not None:
                tweet_info = mentions[i].text.splitlines()
                when = str(tweet_info[3])
                if when.endswith('m') or when.endswith('s') or (when.endswith('h') and int(when[:-1]) <= 24):
                    # knowing that this script will run one time each day
                    crypto = (tweet_info[7].replace(" ", "")).upper()
                    print(crypto)
                    crypto_coin_symbols = [
                        "BTC", "ETH", "BNB", "ADA", "XRP", "SOL", "DOT", "DOGE", "LUNA", "LINK",
                        "LTC", "BCH", "USDC", "WBTC", "MATIC", "XLM", "THETA", "FIL", "VET",
                        "AVAX", "USDT", "ATOM", "TRX", "ICP", "DAI", "EGLD", "XTZ", "CEL", "FTT",
                        "SUSHI", "CRO", "HT", "AAVE", "COMP", "FTM", "TFUEL", "KLAY", "MKR",
                        "XEM", "DCR", "KSM", "DASH", "WAVES", "SNX", "ZEC", "HBAR", "FLOW", "GOV",
                        "YFI", "CHZ", "GRT", "BAT", "RVN", "STX", "ENJ", "UST", "CHIA", "CELO",
                        "ZIL", "NEXO", "HNT", "PAX", "QTUM", "MANA", "HOT", "PUNDIX", "NEXO", "EOS"]
                    if crypto in crypto_coin_symbols:
                        price = (str(cryptocompare.get_price('CRO', 'USD')).split())[2]
                        mentions[i].click()
                        time.sleep(3)
                        input_field_reply = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
                        input_field_reply.click()
                        input_field_reply.send_keys('Now, the price of ' + crypto + ' is ' + price[:-2] + '$')
                        tweet = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')
                        tweet.click()
                        driver.back()
        except IndexError:
            print("end, tadaaa :) ")
            break


login('Xcryptobot', 'wyjKiz-pibgyn-poxwi2')
reply()


