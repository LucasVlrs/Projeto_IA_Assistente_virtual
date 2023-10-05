from project_NATA import *
import unittest

CHAMANDO_NATA_E_PERGUNTA1= f'AI_project_Nata/voice_recordings_for_tests/teste_nome_nata_e_pergunta_1.wav'
CHAMANDO_LUCAS= f'AI_project_Nata/voice_recordings_for_tests/teste_nome_lucas.wav'
PERGUNTA2= f'AI_project_Nata/voice_recordings_for_tests/teste_pergunta_2.wav'
PERGUNTA3= f'AI_project_Nata/voice_recordings_for_tests/teste_pergunta_3.wav'
PERGUNTA4= f'AI_project_Nata/voice_recordings_for_tests/teste_pergunta_4.wav'
PERGUNTA5= f'AI_project_Nata/voice_recordings_for_tests/teste_pergunta_5.wav'
PERGUNTA_INEXISTENTE= f'AI_project_Nata/voice_recordings_for_tests/teste_pergunta_inexistente.wav'

class TestNomeDaAssistente(unittest.TestCase):

    def setUp(self):
        self.nome_do_assistente, self.perguntas_e_respostas  = start()
        
    def test_01_reconhecer_Nata(self):
        transcricao = get_voice_recording(CHAMANDO_NATA_E_PERGUNTA1)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertTrue(valido)
    
    def test_02_nao_reconhecer_Lucas(self):
        transcricao = get_voice_recording(CHAMANDO_LUCAS)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertFalse(valido)

class TestPerguntas(unittest.TestCase):
    
    def setUp(self):
        self.nome_do_assistente, self.perguntas_e_respostas  = start()  

    def test_01_pergunta_1(self):
        transcricao = get_voice_recording(CHAMANDO_NATA_E_PERGUNTA1)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertTrue(valido)
        
    def test_02_pergunta_2(self):
        transcricao = get_voice_recording(PERGUNTA2)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertTrue(valido)
        
    def test_03_pergunta_3(self):
        transcricao = get_voice_recording(PERGUNTA3)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertTrue(valido)
        
    def test_04_pergunta_4(self):
        transcricao = get_voice_recording(PERGUNTA4)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertTrue(valido)
        
    def test_05_pergunta_5(self):
        transcricao = get_voice_recording(PERGUNTA5)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertTrue(valido)
    
    def test_06_pergunta_inexistente(self):
        transcricao = get_voice_recording(PERGUNTA_INEXISTENTE)
        
        transcricao_= str(transcricao).replace("[", "").replace("]", "").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("True", "")
        
        tokens= tokenize_converted_audio(transcricao_)
        self.assertIsNotNone(tokens)
        
        tokens_filtrados= eliminate_stopwords(tokens)
        self.assertIsNotNone(tokens_filtrados)
        
        valido, _= validate_command(tokens_filtrados, self.nome_do_assistente, self.perguntas_e_respostas)
        
        self.assertFalse(valido)
        
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    tests = unittest.TestSuite()
    
    tests.addTest(carregador.loadTestsFromTestCase (TestNomeDaAssistente))  
    tests.addTest(carregador.loadTestsFromTestCase (TestPerguntas))
    
    executor = unittest.TextTestRunner()
    executor.run(tests)