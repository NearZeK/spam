import pyautogui as pg
import time
import io
import pyperclip

time.sleep(5)

txt = io.open("text-nzk.txt", mode="r", encoding="utf-8")

text = ""

for i in txt:
  str = text + i
  pyperclip.copy(str)
  pg.hotkey("ctrl", "v")
  pg.press('Enter')