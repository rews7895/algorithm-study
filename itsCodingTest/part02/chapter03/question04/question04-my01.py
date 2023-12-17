from modules.ProgramTimer import ProgramTimer
# 내 풀이
n, k = map(int, input().split())

timer = ProgramTimer()
cnt = 0
while True:
    x, y = divmod(n, k)
    if y == 0 and x != n:
        n = x
    else:
        n -= 1
    cnt += 1
    if n <= 1:
        break

print(cnt)
timer.timerEnd()




