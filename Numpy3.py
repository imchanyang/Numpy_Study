# Numpy의 활용
# Numpy의 저장과 불러오기

# 단일 객체 저장 및 불러오기
import numpy as np
array = np.arange(0, 10)
print(array)

# 해당 파일은 압축된 형태로 저장되어서 텍스트파일로봐도 보기 어렵다
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)

# 복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1=array1, array2=array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(array1)
print(array2)
print(result1)
print(result2)