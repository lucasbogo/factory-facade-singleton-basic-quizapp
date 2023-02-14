import json
from abc import ABC, abstractmethod

# QuestionFactory é uma classe que cria instâncias de outras classes
class QuestionFactory:
    # Singleton. Aqui ele cria uma instância da classe QuestionFactory
    _instance = None

    # aqui ele cria o construtor da classe
    def __new__(cls):
        # aqui ele verifica se a instância já foi criada, se não, ele cria uma nova instância
        if cls._instance is None:
            # aqui ele cria uma nova instância da classe QuestionFactory
            cls._instance = super().__new__(cls)
        # aqui ele retorna a instância
        return cls._instance

    # aqui ele cria o método create_question, que recebe o question_data como parâmetro
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


# aqui ele cria a classe MultipleChoiceQuestion 
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

# aqui ele cria a classe TrueFalseQuestion 
class TrueFalseQuestion:
    # aqui ele cria o construtor da classe, passando o question_data como parâmetro
    def __init__(self, question_data):
        # aqui ele cria os atributos da classe

        # question_data é um dicionário, então ele pega o valor da chave question e atribui ao atributo prompt
        self.prompt = question_data["question"]
        # aqui ele pega o valor da chave answer e atribui ao atributo answer
        self.answer = question_data["answer"]

# aqui ele cria a classe QuizInterface, que é uma classe abstrata. 
# Serve para definir os métodos que as classes que herdam dela devem ter
class QuizInterface(ABC):
    @abstractmethod
    def take(self):
        pass

    @abstractmethod
    def get_questions(self):
        pass

# aqui ele cria a classe Quiz, que herda da classe QuizInterface.
# serve para criar instâncias de quizzes
class Quiz(QuizInterface):
    # aqui ele cria o construtor da classe, passando o question_factory como parâmetro
    def __init__(self, question_factory):
        # aqui ele cria o atributo question_factory e atribui o question_factory passado como parâmetro
        self.question_factory = question_factory
        # aqui ele cria o atributo questions e atribui uma lista vazia
        self.questions = []

    # aqui ele cria o método load_questions, que recebe o question_data como parâmetro
    def load_questions(self, question_data):
        # aqui ele percorre a lista de dicionários questions dentro do dicionário question_data
        for question in question_data["questions"]:
            # aqui ele adiciona uma instância de MultipleChoiceQuestion ou TrueFalseQuestion na lista questions
            self.questions.append(
                # aqui ele cria uma instância de MultipleChoiceQuestion ou TrueFalseQuestion passando o question como parâmetro para o construtor
                self.question_factory.create_question(question))

    # aqui ele cria o método take, que não recebe parâmetro. serve para fazer o usuário responder as perguntas
    def take(self):
        # aqui ele cria o atributo score e atribui o valor 0
        score = 0
        # aqui ele percorre a lista de perguntas
        for question in self.questions:
            # aqui ele verifica se a pergunta é uma instância de MultipleChoiceQuestion
            if isinstance(question, MultipleChoiceQuestion):
                # aqui ele cria o atributo user_answer e atribui o valor da resposta do usuário
                user_answer = input(
                    # aqui ele imprime a pergunta e as opções de resposta
                    question.prompt + " " + str(question.choices))
            else:
                # aqui ele cria o atributo user_answer e atribui o valor da resposta do usuário
                user_answer = input(question.prompt + " (True/False)")
            # aqui ele verifica se a resposta do usuário é igual a resposta correta
            if user_answer.lower() == str(question.answer):
                # aqui ele incrementa o valor do atributo score 
                score += 1

        # aqui ele imprime o resultado do quiz
        print("You got " + str(score) + "/" +
              str(len(self.questions)) + " correct")

    # aqui ele cria o método get_questions, que não recebe parâmetro
    def get_questions(self):
        # aqui ele retorna a lista de perguntas
        return self.questions

# QuizFacade é uma classe que serve para encapsular a lógica de criação de perguntas e de um quiz
class QuizFacade:
    # aqui ele cria o construtor da classe, passando o quiz_data_filename como parâmetro
    def __init__(self, quiz_data_filename):
        # aqui ele cria o atributo quiz_data e atribui o valor do arquivo json
        with open(quiz_data_filename) as f:
            # aqui ele cria o atributo quiz_data e atribui o valor do arquivo json
            quiz_data = json.load(f)
        # aqui ele cria o atributo question_factory e atribui uma instância de QuestionFactory
        self.quiz_data = quiz_data
        # aqui ele cria o atributo quiz e atribui uma instância de Quiz
        self.question_factory = QuestionFactory()
        # aqui ele cria o atributo quiz e atribui uma instância de Quiz
        self.quiz = Quiz(self.question_factory)
        # aqui ele chama o método load_questions passando o quiz_data como parâmetro
        self.quiz.load_questions(self.quiz_data)

    # aqui ele cria o método take_quiz, que não recebe parâmetro. Serve para chamar o método take do quiz
    def take_quiz(self):
        # aqui ele chama o método take do atributo quiz
        self.quiz.take()

    # aqui ele cria o método get_questions, que não recebe parâmetro. Serve para retornar as perguntas do quiz
    def get_questions(self):
        # aqui ele retorna a lista de perguntas do quiz
        return self.quiz.get_questions()

# finalmente, aqui ele cria a instância da classe QuizFacade e atribui ao atributo quiz_facade com o nome do arquivo json
if __name__ == "__main__":
    # aqui ele cria a instância da classe QuizFacade e atribui ao atributo quiz_facade com o nome do arquivo json
    quiz_facade = QuizFacade("questions.json")
    # aqui ele chama o método take_quiz do atributo quiz_facade
    quiz_facade.take_quiz()
    # aqui ele imprime a lista de perguntas do quiz
    print(quiz_facade.get_questions())