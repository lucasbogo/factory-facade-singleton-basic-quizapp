import json
from abc import ABC, abstractmethod

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


class TrueFalseQuestion:
    # aqui ele cria o construtor da classe, passando o question_data como parâmetro
    def __init__(self, question_data):
        # aqui ele cria os atributos da classe

        # question_data é um dicionário, então ele pega o valor da chave question e atribui ao atributo prompt
        self.prompt = question_data["question"]
        # aqui ele pega o valor da chave answer e atribui ao atributo answer
        self.answer = question_data["answer"]



class QuizInterface(ABC):
    @abstractmethod
    def take(self):
        pass

    @abstractmethod
    def get_questions(self):
        pass


class Quiz(QuizInterface):
    def __init__(self, question_factory):
        self.question_factory = question_factory
        self.questions = []

    def load_questions(self, question_data):
        for question in question_data["questions"]:
            self.questions.append(
                self.question_factory.create_question(question))

    def take(self):
        score = 0
        for question in self.questions:
            if isinstance(question, MultipleChoiceQuestion):
                user_answer = input(
                    question.prompt + " " + str(question.choices))
            else:
                user_answer = input(question.prompt + " (True/False)")
            if user_answer.lower() == str(question.answer):
                score += 1

        print("You got " + str(score) + "/" +
              str(len(self.questions)) + " correct")
    
    def get_questions(self):
        return self.questions
    
class QuizFacade:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.question_factory = QuestionFactory()
        self.quiz = Quiz(self.question_factory)
        self.quiz.load_questions(self.quiz_data)

    def take_quiz(self):
        self.quiz.take()

    def get_questions(self):
        return self.quiz.get_questions()

# finalmente, aqui ele cria a instância da classe QuizFacade e atribui ao atributo quiz_facade com o nome do arquivo json
if __name__ == "__main__":
    quiz_facade = QuizFacade("questions.json")
    # aqui ele usa o método take_quiz da classe QuizFacade para iniciar o quiz
    quiz_facade.take_quiz()
