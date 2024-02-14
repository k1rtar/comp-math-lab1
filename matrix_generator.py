import random

def generate_random_matrix(size):
    matrix = [[random.randint(-10, 10) for _ in range(size)] for _ in range(size)]
    vector = [random.randint(-10, 10) for _ in range(size)]
    return matrix, vector
