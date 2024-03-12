# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2021/10/24 19:56'

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
# trainer.train("chatterbot.corpus.chinese")

# Get a response to an input statement
text = input("请输入您想说的话,退出请输入-1")
while text != '-1':
    response = chatbot.get_response(text)
    print(response)
    text = input()

