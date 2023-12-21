li = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(li)):
    # 가장 작은 원소의 인덱스
    min_index = i
    for j in range(i + 1, len(li)):
        if li[min_index] > li[j]:
            min_index = j
    # 스와프
    li[i], li[min_index] = li[min_index], li[i]

print(li)