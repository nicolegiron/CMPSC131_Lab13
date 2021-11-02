# Author: Nicole Giron nqg5259@psu.edu
# Collaborator: Trey Fishburn thf5044@psu.edu
# Collaborator: Kaitlyn Byrnes krb5906@psu.edu
# Collaborator: Taoran Sheng tps5616@psu.edu
# Section: 4
# Breakout: 4

from matplotlib import pyplot as plt
from sys import argv
import csv

# Retrieve a list of counties from argv[2]
counties = argv[2].split()

# Retrieve the number of days from argv[3]
days = int(argv[3])

plt.xticks(rotation=70, fontsize=6)
plt.ylabel('7-day Average New Cases per 100,000 population')

# Write code to read csv file (argv[1]) into a list of dictionaries
with open(argv[1], newline = '') as f:
  csv = csv.DictReader(f, dialect = 'excel')
  l = []
  for row in csv:
    l.append(row)

for county in counties: 
  # Retrieve from the csv file's data x/y data for a specific county 
  # The length of the data should match the number of days from argv[3]
  # It should be data for the most recent days.
  xData = []
  yData = []

  for i in l:
    if i['Jurisdiction'] == county:
      if i['7-Day Average New Case Rate'] != "":
        xData.append(i['Date'])
        yData.append(float(i['7-Day Average New Case Rate']))

  county_ys = yData[-days:] 
  county_dates = xData[-days:] 
  plt.plot(county_ys, label = county)
  if days > 30:
    plt.xticks(range(0,days,7), county_dates[::7])
  else:
    plt.xticks(range(days), county_dates)


plt.legend()
# Save figure to the file argv[4]
plt.savefig(argv[4])
plt.show()
