import numpy as np


# Function to calculate the sum of a row in the coefficient matrix
def row_sum(coefficient_matrix, independent_terms, row, current_x):
    sum_result = 0
    for j in range(len(coefficient_matrix)):
        sum_result += coefficient_matrix[row, j] * current_x[j]
    return sum_result

# Function to check the convergence of Gauss-Jacobi method
def check_convergence_gauss_jacobi(coefficient_matrix, calculated_x, independent_terms, tolerance=1e-6):
    n = len(coefficient_matrix)

    for i in range(n):
        row_sum_result = row_sum(coefficient_matrix, independent_terms, i, calculated_x)
        difference = abs(row_sum_result - independent_terms[i])
        if difference > tolerance:
            return False
    return True

# Function to solve a system of linear equations using Gauss-Jacobi method
def gauss_jacobi(coefficient_matrix, independent_terms, max_iterations=1000, tolerance=1e-6):
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
    return None, max_iterations  # Returns None if convergence is not achieved


def matrix_from_file(file_name):
    #Matrix Pattern
    #Example File
    # 1 : 2 3
    # 2 : 1
    # 3 : 1 2
    # Matrix
    # Chance per line(exception: diagonal (matrix[i,i])) = 1/number of columns - 0.1
    # Matrix example
    # -1 1/2 1/2 
    # 1/1 -1 0
    # 1/2 1/2 -1
    #Code:
    with open(file_name) as f:
        lines = f.readlines()
        matrix = np.zeros((len(lines), len(lines)))

        for enum, line in enumerate(lines):
            line = line.split(":")
            line = line[1].split()
            for i in range(len(line)):
                division = 1/len(line)
                matrix[enum][int(line[i])-1] = division - 0.1
            matrix[enum][enum] = -1

            
       
        return matrix

def length_from_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return len(lines)

def generate_independent_terms(file_name):
    #return np.zeros(length_from_file(file_name))
    return -1 * np.ones(length_from_file(file_name))

def get_highest_value_index(array):
    highest = 0
    index = 0
    for i in range(len(array)):
        if array[i] > highest:
            highest = array[i]
            index = i
    return index, highest

def main():
    CASES = ["caso000.txt", "caso100.txt", "caso020.txt", "caso050.txt", "caso100.txt", "caso200.txt"]

    for case in CASES:
        print("\nCase:", case)
        #file = "caso000.txt"
        file = case
        matrix = matrix_from_file(file)
        independent_terms = generate_independent_terms(file)
        #print(matrix)

        solution, iterations = gauss_jacobi(matrix, independent_terms)
        if solution is not None:
            print("Solution found after", iterations, "iterations")
            #print(solution)
            #print ("Checking solution:")
            #print (" Original Independent Terms: ", independent_terms)
            #print(" Obtained Values using the Solution: ", np.dot(matrix, solution))
            highest_index, highest_value = get_highest_value_index(solution)
            highest_value = "{:.2f}".format(highest_value)
            print ("Most Popular Granny:", highest_index + 1, " with", highest_value, "gossips")
        else:
            print("Gauss-Jacobi method did not converge after", iterations, "iterations.")


if __name__ == "__main__":
    main()