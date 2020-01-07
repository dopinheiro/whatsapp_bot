import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class bot():
  def setup(self):
    self.driver = webdriver.Firefox(webdriver.FirefoxProfile('/home/diego/.mozilla/firefox/3u1fhf1t.default'))
  
  def close(self):
    self.driver.quit()
  
  def open_page(self):
    self.driver.get("https://web.whatsapp.com")
    self.driver.set_window_size(683, 728)

  def select_contact(self, contact):
    self.wait= WebDriverWait(self.driver, 20)
    self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='side']/div/div/label/input")))
    self.driver.find_element(By.XPATH, "//div[@id='side']/div/div/label/input").send_keys(contact)
    self.driver.find_element(By.XPATH, "//div[@id='side']/div/div/label/input").send_keys(Keys.ENTER)

  def send_msg(self,message):
    self.driver.find_element(By.XPATH, "//div[@id='main']/footer/div/div[2]/div/div[2]").send_keys(message)
    time.sleep(5)
    self.driver.find_element(By.XPATH, "//div[@id=\'main\']/footer/div/div[3]/button").click()


contact = input('Insira o nome do contato: ')
message = input('Insira a mensagem a ser enviada: ')

whatsapp = bot()
whatsapp.setup()
print('Aguardando autenticação...')
whatsapp.open_page()
whatsapp.select_contact(contact)
whatsapp.send_msg(message)



