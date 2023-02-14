import json
from abc import ABC, abstractmethod

# o QuestionFactory é um factory, ele cria objetos de acordo com o tipo de pergunta...

# question factory com padrão de projeto Singleton. 
# O que o singleton faz é garantir que só exista uma instância de uma classe em todo o programa.
# Aqui ele cria uma classe chamada QuestionFactory e cria um atributo 
# estático chamado _instance para armazenar a instância da classe e garantir que só exista uma instância da classe
class QuestionFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def create_question(question_data):
        # se o tipo for multiple_choice (multipla escolha), ele cria uma instância de MultipleChoiceQuestion
        if question_data["type"] == "multiple_choice":
            # aqui ele retorna uma instância de MultipleChoiceQuestion passando o question_data como parâmetro para o construtor
            return MultipleChoiceQuestion(question_data)
        # se o tipo for true_false (verdadeiro ou falso), ele cria uma instância de TrueFalseQuestion
        elif question_data["type"] == "true_false":
            # aqui ele retorna uma instância de TrueFalseQuestion passando o question_data como parâmetro para o construtor
            return TrueFalseQuestion(question_data)
        else:
            # se o tipo não for nenhum dos dois, ele lança uma exceção
            raise ValueError("Invalid question type")

# Parte do padrão de projeto Factory, aqui ele cria uma classe para cada tipo de pergunta, neste caso, MultipleChoiceQuestion
class MultipleChoiceQuestion:
    # aqui ele cria o construtor da classe, passando o question_data como parâmetro
    def __init__(self, question_data):
        # aqui ele cria os atributos da classe...
        # question_data é um dicionário, então ele pega o valor da chave question e atribui ao atributo prompt
        self.prompt = question_data["question"]
        # aqui ele pega o valor da chave options e atribui ao atributo choices
        self.choices = question_data["options"]
        # aqui ele pega o valor da chave answer e atribui ao atributo answer
        self.answer = question_data["answer"]

# Parte do padrão de projeto Factory, aqui ele cria uma classe para cada tipo de pergunta, neste caso, TrueFalseQuestion


class TrueFalseQuestion:
    # aqui ele cria o construtor da classe, passando o question_data como parâmetro
    def __init__(self, question_data):
        # aqui ele cria os atributos da classe

        # question_data é um dicionário, então ele pega o valor da chave question e atribui ao atributo prompt
        self.prompt = question_data["question"]
        # aqui ele pega o valor da chave answer e atribui ao atributo answer
        self.answer = question_data["answer"]

# Parte do padrão de projeto Facade, aqui ele cria uma classe para facilitar a criação de um quiz


class Quiz:
    # aqui ele cria o construtor da classe, passando o question_factory como parâmetro
    def __init__(self, question_factory):
        # aqui ele cria os atributos da classe...
        # question_factory é uma instância de QuestionFactory, então ele atribui ao atributo question_factory a instância passada como parâmetro
        self.question_factory = question_factory
        # aqui ele cria uma lista vazia e atribui ao atributo questions (lista de perguntas)
        self.questions = []

        # aqui ele cria o método load_questions, passando o question_data como parâmetro (question_data é um dicionário)
    def load_questions(self, question_data):
        # aqui ele percorre a lista de perguntas (question_data["questions"]) e para cada pergunta, ele cria uma instância de MultipleChoiceQuestion ou TrueFalseQuestion
        for question in question_data["questions"]:
            # entao ele adiciona a instância criada na lista de perguntas (self.questions) usando o método append
            self.questions.append(
                # aqui ele usa o método create_question da classe QuestionFactory para criar uma instância de MultipleChoiceQuestion ou TrueFalseQuestion
                self.question_factory.create_question(question))

        # aqui ele cria o método take, que é o método que inicia o quiz (ele pergunta as perguntas e mostra o resultado)
    def take(self):
        # aqui ele cria uma variável score e atribui o valor 0
        # que será usado para contar o número de perguntas respondidas corretamente
        score = 0
        # aqui ele percorre a lista de perguntas (self.questions) e para cada pergunta, ele pergunta ao usuário a resposta
        for question in self.questions:
            # aqui ele verifica se a pergunta é do tipo MultipleChoiceQuestion
            if isinstance(question, MultipleChoiceQuestion):
                # aqui ele pergunta ao usuário a resposta e atribui o valor digitado pelo usuário à variável user_answer
                # e converte para minúsculo
                user_answer = input(
                    question.prompt + " " + str(question.choices))
                # aqui ele verifica se a pergunta é do tipo TrueFalseQuestion
            else:
                # aqui ele pergunta ao usuário a resposta e atribui o valor digitado pelo usuário à variável user_answer
                user_answer = input(question.prompt + " (True/False)")
                # se a resposta digitada pelo usuário for igual à resposta correta, ele adiciona 1 ao score
                # e mostra a mensagem " voce acertou tanto de tanto"
            if user_answer.lower() == str(question.answer).lower():
                score += 1
        print("You scored " + str(score) +
              " out of " + str(len(self.questions)))

# Parte do padrão de projeto Facade, aqui ele cria uma classe para facilitar a criação de um quiz
# O padrão de projeto Facade é um padrão de projeto estrutural que fornece uma interface simplificada para uma biblioteca,
# um framework ou qualquer outro conjunto complexo de classes.
# serve para simplificar a interface de um conjunto de classes, bibliotecas ou qualquer outro conjunto complexo de classes


class QuizFacade:
    # aqui ele cria o construtor da classe, passando o question_data_file como parâmetro
    def __init__(self, file):
        # aqui ele cria os atributos da classe...
        # question_data_file é o nome do arquivo json que contém as perguntas
        # então ele cria uma instância de QuestionFactory e atribui ao atributo question_factory
        self.question_factory = QuestionFactory()
        # with open... serve para abrir o arquivo json e atribui o conteúdo do arquivo json à variável file
        with open("questions.json", "r") as file:
            # aqui ele usa o método json.load para carregar o conteúdo do arquivo json e atribui ao atributo question_data
            self.question_data = json.load(file)

        # aqui ele cria o método take_quiz, que é o método que inicia o quiz (ele pergunta as perguntas e mostra o resultado)
    def take_quiz(self):
        # aqui ele cria uma instância de Quiz e atribui ao atributo quiz
        quiz = Quiz(self.question_factory)
        # aqui ele usa o método load_questions da classe Quiz para carregar as perguntas
        quiz.load_questions(self.question_data)
        # finalmente, aqui ele usa o método take da classe Quiz para iniciar o quiz
        quiz.take()

# finalmente, aqui ele cria a instância da classe QuizFacade e atribui ao atributo quiz_facade com o nome do arquivo json
if __name__ == "__main__":
    # aqui ele cria uma instância da classe QuizSingleton e atribui ao atributo quiz_singleton
    quiz_facade = QuizFacade("questions.json")
    # aqui ele usa o método take_quiz da classe QuizFacade para iniciar o quiz
    quiz_facade.take_quiz()
