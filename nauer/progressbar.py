
def print_progress_bar(percent, length=80, spinner=[]):
    effective_length = length - 6
    progress = int(effective_length / 100 * percent)

    # spinner must be a mutable to save state between different function calls
    if not spinner:
        spinner.append("/")

    if spinner[0] == "/":
        spinner[0] = "-"
    elif spinner[0] == "-":
        spinner[0] = "\\"
    else:
        spinner[0] = "/"

    print(("\r{0}{1:<" + str(effective_length) + "}{2:>4}%").format(spinner[0], progress * "#", percent), end="")

import time

for i in range(0,100,10):
    print_progress_bar(i, 50)
    time.sleep(1)
    print_progress_bar(i, 50)
    time.sleep(1)

print_progress_bar(100, 50)
