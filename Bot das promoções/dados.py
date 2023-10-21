from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

def promocoeshoje():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    navegador.get('https://www.pelando.com.br/mais-quentes')
    sleep(3)

    ocultar_expiradas = navegador.find_element(By.XPATH,'//input[@class="sc-gRtvSG eaLWft"]').click()

    quentes_de_periodo_dropdown = navegador.find_element(By.XPATH,'//i[@class="sc-gEvEer dEycxP sc-2407acc8-1 besXSB"]').click()
    quentes_de_hoje = navegador.find_element(By.XPATH,'//button[@class="sc-317bc911-4 jChmTt"]').click()
    quentes_de_periodo_fechar = navegador.find_element(By.XPATH,'//i[@class="sc-gEvEer dEycxP sc-317bc911-3 gxafWm"]').click()

    navegador.minimize_window()
    sleep(3)

    titulos_promocoes = navegador.find_elements(By.XPATH,'//a[@class="sc-hknOHE ejDEOj"]')
    preco_promocoes = navegador.find_elements(By.XPATH,'//div[@class="sc-kdBSHD eejzNH sc-gFAWRd dSdBUv"]')
    vendido_por_promocoes = navegador.find_elements(By.XPATH,'//a[@class="sc-Nxspf lpfyf"]')

    lista_titulos_promocoes = [c.text for c in titulos_promocoes]
    lista_preco_promocoes = [d.text for d in preco_promocoes]
    lista_vendido_por_promocoes = [e.text for e in vendido_por_promocoes]

    promocao = zip(lista_titulos_promocoes, lista_preco_promocoes, lista_vendido_por_promocoes)
    
    return promocao

def promocoessemana():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    navegador.get('https://www.pelando.com.br/mais-quentes')
    sleep(3)

    ocultar_expiradas = navegador.find_element(By.XPATH,'//input[@class="sc-gRtvSG eaLWft"]').click()

    # quentes_de_periodo_dropdown = navegador.find_element(By.XPATH,'//i[@class="sc-gEvEer dEycxP sc-2407acc8-1 besXSB"]').click()
    # quentes_de_hoje = navegador.find_element(By.XPATH,'//button[@class="sc-317bc911-4 jChmTt"]').click()
    # quentes_de_periodo_fechar = navegador.find_element(By.XPATH,'//i[@class="sc-gEvEer dEycxP sc-317bc911-3 gxafWm"]').click()

    navegador.minimize_window()
    sleep(3)

    titulos_promocoes = navegador.find_elements(By.XPATH,'//a[@class="sc-hknOHE ejDEOj"]')
    preco_promocoes = navegador.find_elements(By.XPATH,'//div[@class="sc-kdBSHD eejzNH sc-gFAWRd dSdBUv"]')
    vendido_por_promocoes = navegador.find_elements(By.XPATH,'//a[@class="sc-Nxspf lpfyf"]')

    lista_titulos_promocoes = [c.text for c in titulos_promocoes]
    lista_preco_promocoes = [d.text for d in preco_promocoes]
    lista_vendido_por_promocoes = [e.text for e in vendido_por_promocoes]

    promocao = zip(lista_titulos_promocoes, lista_preco_promocoes, lista_vendido_por_promocoes)
    
    return promocao

def promocoesmes():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)

    navegador.get('https://www.pelando.com.br/mais-quentes')
    sleep(3)

    ocultar_expiradas = navegador.find_element(By.XPATH,'//input[@class="sc-gRtvSG eaLWft"]').click()

    quentes_de_periodo_dropdown = navegador.find_element(By.XPATH,'//i[@class="sc-gEvEer dEycxP sc-2407acc8-1 besXSB"]').click()
    quentes_do_mes = navegador.find_elements(By.XPATH,'//button[@class="sc-317bc911-4 jChmTt"]')[2].click()
    quentes_de_periodo_fechar = navegador.find_element(By.XPATH,'//i[@class="sc-gEvEer dEycxP sc-317bc911-3 gxafWm"]').click()

    # navegador.minimize_window()
    sleep(3)

    titulos_promocoes = navegador.find_elements(By.XPATH,'//a[@class="sc-hknOHE ejDEOj"]')
    preco_promocoes = navegador.find_elements(By.XPATH,'//div[@class="sc-kdBSHD eejzNH sc-gFAWRd dSdBUv"]')
    vendido_por_promocoes = navegador.find_elements(By.XPATH,'//a[@class="sc-Nxspf lpfyf"]')

    lista_titulos_promocoes = [c.text for c in titulos_promocoes]
    lista_preco_promocoes = [d.text for d in preco_promocoes]
    lista_vendido_por_promocoes = [e.text for e in vendido_por_promocoes]

    promocao = zip(lista_titulos_promocoes, lista_preco_promocoes, lista_vendido_por_promocoes)
    
    return promocao