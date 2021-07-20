# Numpy는 다차원 배열을 효과적으로 처리할 수 있도록 도와주는 도구입니다.
# Numpyu의 차원
# 1차원 축(행) axis 0, 2차원 축(열) axis 1, 3차원 축(채널) axis 2

import numpy as np

list_data = [1, 2, 3]
print(list_data)

array = np.array(list_data)
print(array)
print(array.size)
print(array.dtype)
print(array[2])
print(array.astype(float))

array1 = np.arange(4)
print(array1)

array2 = np.zeros((4, 4), dtype=float)
print(array2)

array3 = np.ones((3, 3), dtype=str)
print(array3)

array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열이다
array5 = np.random.normal(0, 1, (3, 3))
print(array5)