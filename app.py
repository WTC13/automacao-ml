import tkinter
from tkinter.tix import Tree
from tkinter.ttk import Treeview
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from tkinter import *
import pandas as pd
from pandastable import Table, TableModel
from tkinter import ttk
from tkinter import filedialog

def chuveiro():
    
    service = Service()
    options = webdriver.ChromeOptions()
    navegador = webdriver.Chrome(service=service, options=options)

    url = "https://lista.mercadolivre.com.br/chuveiro"
    navegador.get(url)
    sleep(5)

    navegador.find_element('xpath','/html/body/div[2]/div[1]/div/div[2]/button[1]').click()
    stockList = []
    valuesList = []
    vendedorList = []
    parcelasList = []
    avaliacaoList = []

    titleElements = navegador.find_elements(By.TAG_NAME, 'a')[140:150]
    titleList = [title.get_attribute('title') for title in titleElements]

    for index in range(len(titleElements)):
        # Reencontre o elemento
        titleElements = navegador.find_elements(By.TAG_NAME, 'a')[140:150]
        title = titleElements[index]

        # Verifique se o elemento ainda está presente no DOM
        if EC.staleness_of(title):
            titleElements = navegador.find_elements(By.TAG_NAME, 'a')[140:150]
            title = titleElements[index]

        title.click()
        sleep(1)

        qtdStock = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for stock in qtdStock:
            stock_text = stock.text  # Obtenha o texto do elemento de estoque
            stockList.append(stock_text)

        # Preço do produto
        valores = navegador.find_element(By.CLASS_NAME, 'andes-money-amount').text.replace('\n', '')
        valuesList.append(valores)

        # Nome do vendedor
        vendedor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendedorList.append(vendedor)

        # Parcelas e Valor
        parcelas = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelasList.append(parcelas)

        # Avaliação
        avaliacao = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliacaoList.append(avaliacao)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)

    dfchuveiro = {
        'Nome:' : stockList,
        'Preço:' : valuesList,
        'Vendedor:' : vendedorList,
        'Parcelas e Valor' : parcelasList,
        'Avaliação:' : avaliacaoList
    }

    dc = pd.DataFrame(dfchuveiro)
    dc.to_csv('shower.csv')

def bicicleta():

    service = Service()
    options = webdriver.ChromeOptions()
    navegador = webdriver.Chrome(service=service, options=options)

    url = "https://lista.mercadolivre.com.br/bicicleta"
    navegador.get(url)
    sleep(5)

    navegador.find_element('xpath','/html/body/div[2]/div[1]/div/div[2]/button[1]').click()
    estoqueList = []
    valoresList = []
    vendorList = []
    parcelaList = []
    avaliationList = []

    bikeElements = navegador.find_elements(By.TAG_NAME, 'a')[180:231:3]

    # Primeiro Produto

    while True:
        navegador.find_element('xpath','//*[@id=":R2l5e6:"]/div[2]/div[1]/a').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)

    # Segundo Produto
        navegador.find_element('xpath','//*[@id=":R4l5e6:"]/div[2]/div[1]/a').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)

    # Terceiro Produto
        navegador.find_element('xpath','//*[@id=":R6l5e6:"]/div[2]/div[1]/a[1]').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break

    # Quarto Produto
    while True:
        navegador.find_element('xpath','//*[@id=":R8l5e6:"]/div[2]/div[1]/a').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break

    # Quinto Produto
    while True:
        navegador.find_element('xpath','//*[@id=":Ral5e6:"]/div[2]/div[1]/a').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break

    # Sexto Produto
    while True:
        navegador.find_element('xpath','//*[@id=":Rcl5e6:"]/div[2]/div[1]/a[1]').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break

    # Setimo Produto
    while True:
        navegador.find_element('xpath','//*[@id=":Rel5e6:"]/div[2]/div[1]/a').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break

    # Oitavo Produto
    while True:
        navegador.find_element('xpath','//*[@id=":Rgl5e6:"]/div[2]/div[2]/a').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break

    # Nono Produto
    while True:
        navegador.find_element('xpath','//*[@id=":Ril5e6:"]/div[2]/div[1]/a[1]').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break

    # Decimo Produto
    while True:
        navegador.find_element('xpath','//*[@id=":Rkl5e6:"]/div[2]/div[1]/a').click()

        qtdestoque = navegador.find_elements(By.CLASS_NAME, 'ui-pdp-title')
        # Adicione seu processamento para qtdStock aqui
        for estoque in qtdestoque:
            estoque_text = estoque.text  # Obtenha o texto do elemento de estoque
            estoqueList.append(estoque_text)

        # Preço do produto
        values = navegador.find_elements(By.CLASS_NAME, 'andes-money-amount')[0:2][1].text.replace('\n','').replace('R$', 'R$ ')
        valoresList.append(values)

        # Nome do vendedor
        vendor = navegador.find_element(By.CLASS_NAME, 'ui-seller-data-header__title').text.replace('Vendido por', '')
        vendorList.append(vendor)

        # Parcelas e Valor
        parcela = navegador.find_element(By.ID, 'pricing_price_subtitle').text.replace('\n','').replace('sem juros', ' sem juros').replace('x', 'x ').replace('R$', 'R$ ')
        parcelaList.append(parcela)

        # Avaliação
        avaliation = navegador.find_element(By.CLASS_NAME, 'ui-pdp-review__rating').text
        avaliationList.append(avaliation)
        

        # Volte para a página anterior se necessário
        navegador.back()
        sleep(1)
        break


    dfbike = {
        'Nome:' : estoqueList,
        'Preço:' : valoresList,
        'Vendedor:' : vendorList,
        'Parcelas e Valor' : parcelaList,
        'Avaliação:' : avaliationList
    }

    dfb = pd.DataFrame(dfbike)
    dfb.to_csv('bike.csv')

# Interface

import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Função para carregar o arquivo CSV
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Função para carregar o arquivo CSV
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    # Ler o arquivo CSV
    df = pd.read_csv(file_path)
    
    # Limpar a treeview existente
    for i in tree.get_children():
        tree.delete(i)
    
    # Atualizar a treeview com os novos dados
    tree["column"] = list(df.columns)
    tree["show"] = "headings"
    
    for column in tree["columns"]:
        tree.heading(column, text=column)
    
    for row in df.itertuples(index=False):
        tree.insert("", "end", values=row)

# Criar a janela principal
root = tk.Tk()
root.title("Visualizador de CSV")

# Estilos para os frames e botões
style = ttk.Style()
style.configure("Black.TFrame", background="black", borderwidth=5, relief="solid")
style.configure("Yellow.TButton", background="yellow", foreground="black", borderwidth=5, relief="solid", font=("Arial", 10, "bold"))

# Configurar o fundo da janela principal como preto
root.configure(bg="black")

# Criar dois frames: um para os botões e outro para a tabela
frame_buttons = ttk.Frame(root, style="Black.TFrame")
frame_buttons.pack(pady=10, padx=10, fill="x")

frame_table = ttk.Frame(root, style="Black.TFrame")
frame_table.pack(pady=10, padx=10, fill="both", expand=True)

# Adicionar botões ao frame dos botões
button_search1 = ttk.Button(frame_buttons, text="Pesquisar Chuveiros", style="Yellow.TButton", command=chuveiro)
button_search1.grid(row=0, column=0, padx=5, pady=5)

button_search2 = ttk.Button(frame_buttons, text="Pesquisar Bicicletas", style="Yellow.TButton", command= bicicleta)
button_search2.grid(row=0, column=1, padx=5, pady=5)

button_load = ttk.Button(frame_buttons, text="Carregar CSV", command=load_csv, style="Yellow.TButton")
button_load.grid(row=0, column=2, padx=5, pady=5)

# Criar o widget Treeview no frame da tabela
tree = ttk.Treeview(frame_table)
tree.pack(fill="both", expand=True, side="left")

# Adicionar um scrollbar ao Treeview
scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Executar a aplicação
root.mainloop()

