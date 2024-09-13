from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BOTAO_LOGIN = {
    "id": 'btnEntrarGovBr',
    "name" : 'btnEntrarGovBr',
    "xpath": '//*[@id="btnEntrarGovBr"]',
    "link text": 'Entrar com gov.br',
    "partial link text": "",
    "tag name": "",
    "class name": "",
    "css selector": ""
}

# Now, wait until the alert is closed
def alert_is_closed(driver):
    try:
        driver.switch_to.alert
        return False  # Alert is still present
    except:
        return True  # Alert is closed

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# Remove the WebDriver signature from navigator
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


# TODO: Implementar acesso à página

driver.get("https://portalinvestidor.tesourodireto.com.br/")


# Set up a WebDriverWait object
wait = WebDriverWait(driver, 10) 

user_wait = WebDriverWait(driver, 60) 

# Execute a JavaScript command.
driver.execute_script("alert('Faça login no Tesouro Direto!');")

# Wait for the alert to be closed
user_wait.until(alert_is_closed)

# Wait for the new window or tab
user_wait.until(EC.url_to_be('https://portalinvestidor.tesourodireto.com.br/MeusInvestimentos'))


# TODO: Implementar loop de coleta de dados
# 
# TODO: Implementar exportação de dados 

driver.quit()
