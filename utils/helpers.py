import math
import random

def get_random_questions(questions_array, array_value):
    
    response = []
    nums = []
    
    for item in range(10):
        random_number = math.ceil(array_value * random.random())
        if random_number in nums:
            ...

        response.push(questions_array[nums[0]])
        response.push(questions_array[nums[1]])
        response.push(questions_array[nums[2]])
        response.push(questions_array[nums[3]])
        response.push(questions_array[nums[4]])
        response.push(questions_array[nums[5]])
        response.push(questions_array[nums[6]])
        response.push(questions_array[nums[7]])
        response.push(questions_array[nums[8]])
        response.push(questions_array[nums[9]])

        return response