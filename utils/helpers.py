import math
import random


def get_random_questions(questions_list):

     random_questions = []

     for item in range(10):
          list_value = len(questions_list) - 1
          random_num = math.ceil(list_value * random.random())
          random_questions.append(questions_list[random_num])
          questions_list.remove(questions_list[random_num])

     return random_questions

