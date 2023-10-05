import requests
from bs4 import BeautifulSoup
import json

def scrap_answers():
    headers= {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition std-1)"}

    lista_respostas= []
    
    # primeira pergunta
    
    url1= "https://www.biologianet.com/anatomia-fisiologia-animal/principais-sistemas-corpo-humano.htm#"
    resposta1 = requests.get(url1)

    soup = BeautifulSoup(resposta1.content, 'html.parser')

    resposta1= soup.find_all("span", class_= "artigo-resumo")

    texto_resposta = resposta1[0].get_text() if resposta1 else ""

    lista_respostas.append({"pergunta": "sistemas", "resposta": texto_resposta})

    #segunda pergunta

    url2= f"https://top10mais.org/top-10-maiores-ossos-do-corpo-humano/"
    resposta2 = requests.get(url2)

    soup2 = BeautifulSoup(resposta2.content, 'html.parser')

    resposta2= soup2.find_all("p")[11]
    
    texto_resposta2= resposta2.get_text() if resposta2 else ""

    lista_respostas.append({"pergunta": "osso", "resposta": texto_resposta2})

    #terceira pergunta
    
    url3= f"https://www.todamateria.com.br/sistema-muscular/#"
    resposta3 = requests.get(url3)

    soup3 = BeautifulSoup(resposta3.content, 'html.parser')

    resposta3= soup3.find_all("p")[4]

    texto_resposta3 = resposta3.get_text() if resposta3 else ""

    lista_respostas.append({"pergunta": "músculos", "resposta": texto_resposta3})

    #quarta pergunta
    
    url4= "https://www.biologianet.com/histologia-animal/principais-tecidos-humanos.htm#"
    resposta4 = requests.get(url4)

    soup = BeautifulSoup(resposta4.content, 'html.parser')

    resposta4= soup.find_all("span", class_= "artigo-resumo")

    texto_resposta = resposta4[0].get_text() if resposta4 else ""

    lista_respostas.append({"pergunta": "tecido", "resposta": texto_resposta})
    
    #quinta pergunta
    
    url5= "https://www.biologianet.com/anatomia-fisiologia-animal/sistema-cardiovascular.htm#"
    resposta5 = requests.get(url5)

    soup = BeautifulSoup(resposta5.content, 'html.parser')

    resposta5= soup.find_all("p")

    texto_resposta = resposta5[7].get_text() if resposta1 else ""

    lista_respostas.append({"pergunta": "coração", "resposta": texto_resposta})
    
    #criar o JSON
    
    json_obj = json.dumps({"nome": "nata", "perguntas_e_respostas" : lista_respostas}, indent=4)

    with open("AI_project_Nata\config.json", "w") as arquivo:
        arquivo.write(json_obj)