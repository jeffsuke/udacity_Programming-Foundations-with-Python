import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on" + time.ctime())

while(break_count < total_breaks):
    time.sleep(1)
    # webbrowser.open("https://www.youtube.com/watch?v=PSksGiZlgV8")
    print(break_count)
    break_count = break_count + 1
