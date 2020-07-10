import numpy as np

arr1 = np.array([[1,2,3], [4,5,6]])
arr2 = np.arange(10)

arr3 = arr2.reshape(-1, 1)

arr4 = np.delete(arr1, (2, 4)) ## 비항구적인 delete를 arr4에 저장해서 항구적으로 사용

arr5 = np.append(arr2, [1,2,3])

arr6 = np.append([[1,2], [3,4]], [[5,6]], axis=1)
print(arr1)

## delete 해서 차원이 떨어지고 거기에 append 하면 어떻게 될가?