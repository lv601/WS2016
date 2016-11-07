
def print_progress_bar(percent, length, spinner=[]):
    #print("percent: ", percent)
    #print("length: ", length)
    #print("spinner: ", spinner)
    effective_length = length - 6
    #print("eff_len: ", effective_length)
    #print("str eff_len: ", str(effective_length))
    progress = int(effective_length / 100 * percent)
    #print(progress)
    #print(spinner)

    # spinner must be a mutable to save state between different function calls
    if not spinner:
        spinner.append("/")
        #print(spinner)

    if spinner[0] == "/":
        spinner[0] = "-"
    elif spinner[0] == "-":
        spinner[0] = "\\"
    else:
        spinner[0] = "/"

    #print("dummy: " + str(effective_length))
    print(("\r{0}{1:.<" + str(effective_length) + "}{2:>4}%").format(spinner[0], progress * "#", percent), end="")

import time

for i in range(0,100,10):
    print_progress_bar(i, 50)
    time.sleep(2)
    print_progress_bar(i, 50)
    time.sleep(2)

print_progress_bar(100, 50)
