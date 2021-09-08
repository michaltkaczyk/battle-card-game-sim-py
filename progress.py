import sys


def print_progress_bar(iteration, total, length_when_filled=20):
    percentage_finished = iteration / total
    filled_length = int(percentage_finished * length_when_filled)
    bar = "#" * filled_length + "-" * (length_when_filled - filled_length)

    sys.stdout.write("\r" + "Progress: [" + bar + "] " + "{:.2%}".format(percentage_finished))
    sys.stdout.flush()

    if iteration == total:
        print()
