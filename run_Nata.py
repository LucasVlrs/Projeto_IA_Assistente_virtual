from project_NATA import *

if __name__ == "__main__":
    pergunta_respondida= False
    
    scrap_answers()
    nome_do_assistente, perguntas_e_respostas= start()
    while pergunta_respondida == False:
        frase = get_audio()
        tokens = tokenize_converted_audio(frase)
        tokens_filtrados= eliminate_stopwords(tokens)
        valido, resposta= validate_command(tokens_filtrados, nome_do_assistente, perguntas_e_respostas)
        if valido: 
            run_command(resposta) 
            pergunta_respondida= True
        else: 
            print("Não sei responder isso. Faça outra pergunta, por favor.") 
            