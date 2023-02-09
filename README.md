# factory-facade-singleton-basic-quizapp

# The code is using several design patterns to structure the program:

# Factory pattern: 
The QuestionFactory class acts as a factory, creating different types of questions based on the data provided. The create_question method takes in a question_data dictionary
and returns an instance of either MultipleChoiceQuestion or TrueFalseQuestion depending on the value
of the type key.
<br>


# Facade pattern: 
The QuizFacade class provides a simplified interface to the functionality of the Quiz and QuestionFactory classes. It reads the question data from a file,
creates a Quiz object with the question factory and loads the questions. It also provides the take_quiz method which is the entry point for taking the quiz.

# Singleton pattern: 
The QuizSingleton is a singleton class, it allows only one instance of the class to exist.

---------------------------------------------------------------------------------------

# O código está a utilizar vários padrões para estruturar o programa:

# Factory: 
A classe QuestionFactory actua como uma fábrica, criando diferentes tipos de perguntas com base nos dados fornecidos. O método create_question inclui um dicionário de dados_de_questões e devolve uma instância de MultipleChoiceQuestion ou TrueFalseQuestion, dependendo do valor da chave do tipo.

# Facade pattern: 
A classe QuizFacade fornece uma interface simplificada para a funcionalidade do Quiz e das classes QuestionFactory. Lê os dados das perguntas de um ficheiro, cria um objecto de Quiz com a fábrica de perguntas e carrega as perguntas. fornece também o método take_quiz, que é o ponto de entrada para a realização do questionário.

# Singleton pattern: 
O QuizSingleton é uma classe de singleton, permite a existência de apenas uma instância da classe.
