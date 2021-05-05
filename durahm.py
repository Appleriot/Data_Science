import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/durham.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, prcps = [], []
    for row in reader:
        currert_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcps = int(row[3])
        except ValueError:
            print(f"Missing data for {currert_date}")
        else:
            dates.append(currert_date)
            prcps.append(prcp)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='red', alpha=0.5)
ax.fill_between(dates, prcps, facecolor='blue', alpha=0.1)

title = 'Durham Chart'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures(f)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()


