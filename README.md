# factory-facade-singleton-basic-quizapp

# três padrões implementado com sucesso.

# O padrão Singleton:

é implementado na classe QuestionFactory onde garante que existe apenas uma instância da classe ao longo de todo o programa.

# O padrão Factory:
é implementado na classe QuestionFactory, pois é responsável pela criação de objectos das classes MultipleChoiceQuestion e TrueFalseQuestion, com base nos dados de entrada.

# O padrão Facade: 
é implementado na classe QuizFacade, que fornece uma interface simplificada à classe Quiz e esconde a complexidade do Quiz e das suas classes subjacentes do cliente. A classe QuizFacade utiliza a classe Quiz e a classe QuestionFacade para carregar perguntas e executar o Quiz.

-----------------------------------------------------------------------------------------------------------------------------
# três padrões parcialmente implementado...

# Factory pattern: 
The QuestionFactory class acts as a factory, creating different types of questions based on the data provided. The create_question method takes in a question_data dictionary
and returns an instance of either MultipleChoiceQuestion or TrueFalseQuestion depending on the value
of the type key.
<br>


# Facade pattern: 
The QuizFacade class provides a simplified interface to the functionality of the Quiz and QuestionFactory classes. It reads the question data from a file,
creates a Quiz object with the question factory and loads the questions. It also provides the take_quiz method which is the entry point for taking the quiz.

# Singleton pattern: 
This code defines a singleton pattern in the QuestionFactory class. The singleton pattern is implemented by using the ```__new__``` method to ensure that only one instance of the class is created. The method checks if an instance of the class has already been created, and if not, it creates a new instance of the class. If an instance has already been created, it returns the existing instance. This ensures that only one instance of the QuestionFactory class exists, and any calls to the create_question method will be made on the same instance of the class.

---------------------------------------------------------------------------------------

# O código está a utilizar vários padrões para estruturar o programa:

# Factory: 
A classe QuestionFactory actua como uma fábrica, criando diferentes tipos de perguntas com base nos dados fornecidos. O método create_question inclui um dicionário de dados_de_questões e devolve uma instância de MultipleChoiceQuestion ou TrueFalseQuestion, dependendo do valor da chave do tipo.

# Facade pattern: 
A classe QuizFacade fornece uma interface simplificada para a funcionalidade do Quiz e das classes QuestionFactory. Lê os dados das perguntas de um ficheiro, cria um objecto de Quiz com a fábrica de perguntas e carrega as perguntas. fornece também o método take_quiz, que é o ponto de entrada para a realização do questionário.

# Singleton pattern: 
Este código define  padrão Singleton na classe QuestionFactory. O Singleton é implementado utilizando o método __novo__ para assegurar que apenas uma instância da classe é criada. O método verifica se uma instância da classe já foi criada, e se não o foi, cria uma nova instância da classe. Se uma instância já tiver sido criada, devolve a instância existente. Isto assegura que apenas uma instância da classe QuestionFactory existe, e quaisquer chamadas para o método create_question serão feitas na mesma instância da classe.
