import speech_recognition as sr
from nltk import word_tokenize, corpus
from bs4 import BeautifulSoup
from config_file_creator import scrap_answers
import json
import requests

CORPUS_LANGUAGE= "portuguese"
LANGUAGE= "pt-BR"
CONFIG_PATH= "AI_project_Nata\config.json"

def start():
    with open(CONFIG_PATH, "r" ) as config_file:
        config= json.load(config_file)    
        nome_do_assistente= config["nome"]
        perguntas_e_respostas= config["perguntas_e_respostas"]
    
    return nome_do_assistente, perguntas_e_respostas

def get_voice_recording(audio): #def exclusiva para testes
    tem_transcricao= False
    reconhecedor= sr.Recognizer()
    with sr.AudioFile(audio) as fonte_de_audio:
        fala= reconhecedor.listen(fonte_de_audio)
        transcricao= reconhecedor.recognize_google(fala, language= LANGUAGE)
        tem_transcricao= True
    return tem_transcricao, transcricao
        
def get_audio():
    
    microfone= sr.Recognizer()

    with sr.Microphone() as audio_source:
        microfone.adjust_for_ambient_noise(audio_source)
        print("Olá, eu sou a Nata, sua assistente virtual.")
        print("O que você deseja saber sobre o corpo humano ?")
        audio= microfone.listen(audio_source)
    try:
        frase= microfone.recognize_google(audio, language= LANGUAGE)
        print("Você perguntou: " + frase + " ?")
    except sr.UnkownValueError:
        print("Não consegui te entender...")
    
    return frase

def tokenize_converted_audio(frase):
    return word_tokenize(frase)

def eliminate_stopwords(tokens):
    palavras_de_parada= set(corpus.stopwords.words(CORPUS_LANGUAGE))
    stopwords_complementares= {"Quantos", "Qual", "Quais","quais","tipos", "corpo", "humano", "função", "existem","compõe", "maior"}
    palavras_de_parada.update(stopwords_complementares)
    
    tokens_filtrados= []

    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

def validate_command(tokens_filtrados, nome_do_assistente, perguntas_e_respostas):
    valido, resposta= False, None

    if len(tokens_filtrados) >= 2:
        if nome_do_assistente.lower() == tokens_filtrados[0].lower():
            pergunta= tokens_filtrados[1]
                
            for lista_json in perguntas_e_respostas:
                if pergunta.lower() == lista_json["pergunta"].lower():
                    resposta= lista_json["resposta"]
                    
                    if resposta == None:
                        print('Não foi possível entender a sua pergunta.')
                        valido= False
                        break
                    else:
                        valido= True
                        break

    return valido, resposta
            
def run_command(resposta):
    print(f'{resposta}')
