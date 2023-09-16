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
def gauss_jacobi(coefficient_matrix, independent_terms, max_iterations=100, tolerance=1e-6):
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

# Example of usage
if __name__ == "__main__":
    coefficient_matrix = np.array([[12, 6, 5],
                                   [1, 8, 4],
                                   [2, 1, 7]])

    independent_terms = np.array([-1, 6, 5])

    solution, iterations = gauss_jacobi(coefficient_matrix, independent_terms)
    if solution is not None:
        print("Solution found after", iterations, "iterations:")
        print(solution)
        print ("Checking solution:")
        print (" Original Independent Terms: ", independent_terms)
        print(" Obtained Values using the Solution: ", np.dot(coefficient_matrix, solution))
    else:
        print("Gauss-Jacobi method did not converge after", iterations, "iterations.")
