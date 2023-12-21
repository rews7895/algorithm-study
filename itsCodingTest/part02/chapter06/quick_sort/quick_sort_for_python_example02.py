li = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(li):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(li) <= 1:
        return li

    # 피벗은 첫 번째 원소
    pivot = li[0]
    # 피벗을 제외한 리스트
    tail = li[1:]

    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x <= pivot]
    # 분할된 오른쪽 부분
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(li))