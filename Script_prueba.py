from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://siu-utl.scalahed.com/usuarios/login")
time.sleep(1)
usuario = driver.find_element(By.XPATH, "//input[@id='id_username']")
clave = driver.find_element(By.CSS_SELECTOR, "input[id='id_password']")
time.sleep(1)
usuario.send_keys("010534512")
time.sleep(1)
clave.send_keys("Pancho2209")
time.sleep(1)
boton=driver.find_element(By.CLASS_NAME, "entrar")
boton.click()
time.sleep(3)
driver.quit()
'''Para id en css selector usa viñeta#id_value y para class viñeta.class_value'''
# varios= driver.find_elements(By.id, id)
#for i in varios:
#i.send_keys("1233443") ejemplos de variuos elementos