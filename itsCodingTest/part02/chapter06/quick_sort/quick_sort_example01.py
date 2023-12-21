li = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(li, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and li[left] <= li[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and li[right] >= li[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            li[right], li[pivot] = li[pivot], li[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            li[left], li[right] = li[right], li[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(li, start, right - 1)
    quick_sort(li, right + 1, end)


quick_sort(li, 0, len(li) - 1)
print(li)
