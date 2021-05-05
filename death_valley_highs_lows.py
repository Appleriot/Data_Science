import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high, and low temps
    dates, highs, lows = [], [], []
    for row in reader:
        currert_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
        except ValueError:
            print(f"Missing data for {currert_date}")
        else:
            dates.append(currert_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low tempautres.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temps -2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures(f)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
