# 내 풀이 1
return_money = 1260
money_unit = {500: 0, 100: 0, 50: 0, 10: 0}
cnt = 0

for key_unit in money_unit.keys():
    unit_cnt = return_money // key_unit
    return_money = return_money % key_unit
    money_unit[key_unit] = unit_cnt
    cnt += unit_cnt
    if return_money <= 0:
        break

print(cnt)

