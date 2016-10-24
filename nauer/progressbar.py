#!/usr/bin/env python3
import time


def print_progress_bar(percent, length=80, spinner_char="/-\\", spinner=[]):
    effective_length = length - 7
    progress = int(effective_length / 100 * percent)

    # spinner must be a mutable to save state between different function calls
    if not spinner:
        spinner.extend(spinner_char)

    c = spinner.pop(0)
    spinner.append(c)

    print(("\r{0} {1:<" + str(effective_length) + "}{2:>4}%").format(c, progress * "#", percent), end="")

if __name__ == "__main__":
    for i in range(0,101,10):
        print_progress_bar(i, 50, spinner_char="abcdefg")
        time.sleep(1)

    # Reset Spinner (Very dirty - We can avoid this with classes)
    print_progress_bar.__defaults__ = (80,"/-\\",[])

    for i in range(0,101,20):
        print_progress_bar(i, 50)
        time.sleep(1)




