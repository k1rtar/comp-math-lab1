class Solver:
    def __init__(self, matrix, vector, precision):
        self.matrix = matrix
        self.vector = vector
        self.precision = precision
        self.size = len(vector)
        self.MAX_NUM_OF_ITERATIONS = 2000

    def is_diagonally_dominant(self):
        for i in range(self.size):
            if abs(self.matrix[i][i]) < sum(abs(self.matrix[i][j]) for j in range(self.size))-abs(self.matrix[i][i]):
                return False
        return True

    def rearrange_matrix(self):
        for i in range(self.size):
            max_element = abs(self.matrix[i][i])
            max_row = i
            for k in range(i+1, self.size):
                if abs(self.matrix[k][i]) > max_element:
                    max_element = abs(self.matrix[k][i])
                    max_row = k
            self.matrix[i], self.matrix[max_row] = self.matrix[max_row], self.matrix[i]
            self.vector[i], self.vector[max_row] = self.vector[max_row], self.vector[i]
        return self.matrix, self.vector

    def vector_multiplication(self,a,b):
        return [a[i] * b[i] for i in range(len(a))]

    def determinant(self, matrix):
        size = len(matrix)
        if size == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        det = 0
        for i in range(size):
            sub_matrix = [row[:i] + row[i+1:] for row in (matrix[:0] + matrix[0+1:])]
            det += ((-1)**i)*matrix[0][i]*self.determinant(sub_matrix)
        return det    

    def solve(self):
        if not self.is_diagonally_dominant():
            self.matrix, self.vector = self.rearrange_matrix()
            if not self.is_diagonally_dominant():
                return None, "Диагональное преобладание не может быть достигнуто.", None

        C = [[-1 * num / line[i] if i != j else 0
              for j, num in enumerate(line)
              ]
             for i, line in enumerate(self.matrix)
             ]
        d = [self.vector[k]/self.matrix[k][k] for k in range(self.size)]
        X = d[:]
        number_of_iterations = 0
        X_table = []
        precision_vector = []
        
        while number_of_iterations<self.MAX_NUM_OF_ITERATIONS:
            max_error = -1
            X_new = [sum(self.vector_multiplication(C[i], X)) + d[i]
                         for i in range(self.size)]
            
            for j in range(self.size):
                max_error = max(max_error,abs(X_new[j]-X[j]))
            precision_vector.append(max_error)
            X_table.append(X_new)
            X = X_new[:]
            number_of_iterations += 1
            if max_error <= self.precision: break
        return X_table,number_of_iterations,precision_vector
