# Numpy의 기본 연산

# Numpy의 상수 연산
import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)
result_array = array * 10
print(result_array)
print(result_array.dtype)

# Numpy의 연산과 함수

# 서로 다른 형태의 Numpy 연산 브로드캐스트 : 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2)
array3 = array1 + array2
print(array1)
print(array2)
print(array3)

array_1 = np.arange(0, 8).reshape(2, 4)
array_2 = np.arange(0, 8).reshape(2, 4)
array_3 = np.concatenate([array_1, array_2], axis=0)
print(array_3)
array_4 = np.arange(0, 4).reshape(4, 1)
print(array_4)
print(array_3 + array_4)


# Numpy의 마스킹 연산
array__1 = np.arange(16).reshape(4, 4)
print(array__1)
array__2 = array__1 < 10
print(array__2)

array__1[array__2] = 100
print(array__1)

# Numpy의 집계 함수
array___1 = np.arange(16).reshape(4, 4)
print(array___1)
print("최대값 : ", np.max(array___1))
print("최소값 : ", np.min(array___1))
print("합계 : ", np.sum(array___1))
print("평균 : ", np.mean(array___1))
print("중앙값 : ", np.median(array___1))

print("합계 : ", np.sum(array___1, axis=0))



