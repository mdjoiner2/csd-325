import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
while True:
    print("Welcome to the weather data visualizer!")
    print("Choose an option:")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == '2':
        # Plot the low temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        input("Press Enter to exit...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")