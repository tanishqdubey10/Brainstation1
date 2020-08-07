import numpy as np
import pandas as pd

Matrix_A = np.random.randn(2,3)
print(Matrix_A)

Matrix_B = np.random.rand(3,4)


final_result = np.matmul(Matrix_A, Matrix_B)
print(final_result.shape)

#party
