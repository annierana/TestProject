# This is a sample Python script
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(message):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi everyone, {message}')  # Press Ctrl+F8 to toggle the breakpoint.
    file1 = pd.read_csv("Planets.csv")
    print(file1.info())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to Data Analytics Class')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
