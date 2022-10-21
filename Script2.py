from typing import List
from time import sleep

last : str = ""

while 1:
    with open("file.txt", "r", encoding="UTF-8") as f:
        file_lines : List[str] = [line.strip() for line in f]
    if last == file_lines[-1]:
        sleep(0.5)
        continue
    last = file_lines[-1]
    print(last)