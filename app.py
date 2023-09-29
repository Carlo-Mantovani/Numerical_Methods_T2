import numpy as np


# Function to calculate the sum of a row in the coefficient matrix
def row_sum(coefficient_matrix, row, current_x):
    sum_result = 0
    for j in range(len(coefficient_matrix)):
        sum_result += coefficient_matrix[row, j] * current_x[j]
    return sum_result

# Function to check the convergence of Gauss-Jacobi method
def check_convergence_gauss_jacobi(coefficient_matrix, calculated_x, independent_terms, tolerance=1e-6):
    n = len(coefficient_matrix)

    for i in range(n):
        row_sum_result = row_sum(coefficient_matrix, i, calculated_x)
        difference = abs(row_sum_result - independent_terms[i])
        if difference > tolerance:
            return False
    return True

# Function to solve a system of linear equations using Gauss-Jacobi method
def gauss_jacobi(coefficient_matrix, independent_terms, max_iterations=1000):
    n = len(coefficient_matrix)

    current_x = np.ones(n)
    next_x = np.zeros(n)

    for iteration in range(max_iterations):
        for i in range(n):
            sum_result = 0
            for j in range(n):
                if j != i:
                    sum_result += coefficient_matrix[i, j] * current_x[j]
            next_x[i] = (independent_terms[i] - sum_result) / coefficient_matrix[i, i]
        current_x[:] = next_x
        if check_convergence_gauss_jacobi(coefficient_matrix, current_x, independent_terms):
            return current_x, iteration + 1
    return current_x, max_iterations  # Returns None if convergence is not achieved


def matrix_from_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        matrix = np.zeros((len(lines), len(lines)))

        for enum, line in enumerate(lines):
            line = line.split(":")
            line = line[1].split()
            for i in range(len(line)):
                division = 1/len(line)
                matrix[int(line[i])-1][enum] = division * 0.9
            matrix[enum][enum] = -1

            
       
        return matrix

# Function to get the length of the file
def length_from_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return len(lines)

# Function to generate the independent terms vector
def generate_independent_terms(file_name):

    return -1 * np.ones(length_from_file(file_name))

# Function to get the index of the highest value in an array
def get_highest_value_index(array):
    highest = 0
    index = 0
    for i in range(len(array)):
        if array[i] > highest:
            highest = array[i]
            index = i
    return index, highest

def main():

    # Select between a specific case or all pre-defined cases
    inputText = input("Select between a specific case or all pre-defined cases (s/a): ")
    if inputText == "s":
        file = input("Enter the file name(Ex: case010.txt): ")
        CASES = [file]
    else:
        CASES = ["case010.txt", "case015.txt", "case020.txt", "case050.txt", "case100.txt", "case200.txt"]

    # Iterate over all cases
    for case in CASES:
        print("\nCase:", case)

        matrix = matrix_from_file(case)
        independent_terms = generate_independent_terms(case)

        solution, iterations = gauss_jacobi(matrix, independent_terms)
        print("Solution found after", iterations, "iterations")
        highest_index, highest_value = get_highest_value_index(solution)
        print ("Most Popular granny is Granny", highest_index + 1, "with", highest_value, "gossips")



if __name__ == "__main__":
    main()