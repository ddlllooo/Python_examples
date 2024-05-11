
from scipy.optimize import linprog
import numpy as np

# 目标函数：max z = 4x1 + 3x2
fval = np.array([4, 3])
# 线性不等式约束条件
A = np.array([[2, 1], [1, 1], [0, 1]])
b = np.array([10, 8, 7])
# 决策变量的下界向量和上界向量
lb = 0
ub = None
# 求解线性规划
res = linprog(c=-fval, A_ub=A, b_ub=b, bounds=((lb, ub), (lb, ub)))
# 输出
print(res)


from scipy.optimize import linprog
import numpy as np

# 目标函数：max z = 4x1 + 3x2
fval = np.array([4, 3])
# 线性不等式约束条件
A = np.array([[2, 1], [1, 1], [0, 1]])
b = np.array([10, 8, 7])
# 决策变量的下界向量和上界向量
lb = 0
ub = None
# 求解线性规划
res = linprog(c=-fval, A_ub=A, b_ub=b, bounds=((lb, ub), (lb, ub)))
# 输出
print(res)

