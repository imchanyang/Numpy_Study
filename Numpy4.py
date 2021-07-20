import numpy as np

# Numpy원소의 정렬
# 오름차순 정렬
array = np.array([5, 9, 10, 3, 1])
print(array)
array.sort()
print(array)
print(array[::-1])

# 각 열을 기준으로 정렬
array_ = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 4]])
print(array)
array_.sort(axis=0)
print(array)

# 균일한 간격으로 데이터 생성(0부터 10사이를 5개 데이터로 채운다)
array__ = np.linspace(0, 10, 5)
print(array_)

# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3)))

# Numpy 배열 객체 복사
array_1 = np.arange(0, 10)
array_2 = array_1
print(array_1)
array_2[0] = 777
print(array_1)

# 행렬 자체가 array_2에 들어간다. 이것을 방지하기위해 np.unique()를 사용한다.
array_3 = array_1.copy()
array_3[0] = 999
print(array_1)

# 중복된 원소 제거
array___ = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array___))