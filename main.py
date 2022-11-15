import time
import datetime
import os
import pyautogui as pg
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

datahora = datetime.now()
datahora1 = datahora.strftime('%H:%M:%S')

pg.alert('Bot ira iniciar após pressionar OK!!!')
while True:
    datahora = datetime.now()
    datahora1 = datahora.strftime('%H:%M:%S')
    os.system('cls')
    if datahora1 == str('08:00:00'):
        navegador.get('SITE')
        time.sleep(3)
        navegador.find_element('xpath', '//*[@id="cpf"]').send_keys('EMAIL')
        time.sleep(3)
        navegador.find_element('xpath', '//*[@id="senha"]').send_keys('SENHA')
        time.sleep(3)
        navegador.find_element('xpath', '//*[@id="login-ponto-web"]/div[3]/div/button').click()
        time.sleep(3)
        navegador.find_element('xpath', '//*[@id="ponto"]/button').click()
        time.sleep(3)
        navegador.find_element('xpath', '//*[@id="marcarponto"]/div/div/div[2]/div/button[2]').click()
        time.sleep(3)


pg.alert('Bot finalizado')
