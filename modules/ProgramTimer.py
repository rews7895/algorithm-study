"""
시간 측정
"""
import time

class ProgramTimer:
  def __init__(self):
    self.start = time.time()
    self.end = 0

  def timerStart(self):
    self.start = time.time()

  def timerEnd(self):
    self.end = time.time() - self.start
    print('실행 시간:', round(self.end, 4), '초')