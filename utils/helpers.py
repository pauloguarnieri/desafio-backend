import math
import random

def get_random_questions(questions_array, array_value):
    res = []
    nums = []
    for i in range(10):
        x = math.ceil(array_value * random.random())
        if x in nums:
            ...

        res.push(questions_array[nums[0]])
        res.push(questions_array[nums[1]])
        res.push(questions_array[nums[2]])
        res.push(questions_array[nums[3]])
        res.push(questions_array[nums[4]])
        res.push(questions_array[nums[5]])
        res.push(questions_array[nums[6]])
        res.push(questions_array[nums[7]])
        res.push(questions_array[nums[8]])
        res.push(questions_array[nums[9]])

        return res