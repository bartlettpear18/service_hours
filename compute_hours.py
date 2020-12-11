import numpy as np
import pandas as pd
import csv

'''
Prereq:
(I just manually went through each line item in the spreadsheet to make sure that the 'hours' column was accurate.
For example, if a brother donated money, they might have just put 0 for hours. So just manually convert the money to hours (donation/10) and put it in this column.)

Download the spreadsheet data of responses to an excel file called "hours.xlsx"
Make sure it's in the same directory/folder as this script

Then call 'python computer_hours.py'
'''


def read_in():

    # These are the "Features" of the spreadsheet data that we're particularly interested in
    features = ["BA", "Hours"]

    # Pandas is a Python package that helps with data exploration. We load the excel file through here
    # Run 'pip install pandas' in the terminal to download it for the first time
    readin = pd.read_excel("hours.xlsx")

    # Filter the data to the features we want (BA and Hours) and fill NaN (empty) values with -1.0
    filtered = pd.DataFrame(readin, columns=features).fillna(-1)

    # Converting a Pandas 'Dataframe' to a Numpy array helps with certain operations
    # Run 'pip install numpy' to get numpy
    # Theoritically this could all be done with Pandas, but when I wrote it, I was more familiar with Numpy
    # Tbh, I forgot why I 'reshaped' the array, but I'm sure there was some error that I had to correct for. Play around with it by commenting it if you want
    arr = filtered.to_numpy().reshape(-1, 2)

    # np.unique parses the first column (b/c of the [:,0] - this is called array indexing/slicing) of the data to determine all the unique brother BA numbers
    brothers = np.unique(arr[:, 0])

    # Empty array to populate with the running totals of brothers/ hours
    brothers_sum = np.zeros((len(brothers), 2))

    i = 0
    for bro in brothers:
        # index is a list of indices (like [0, 4, 127...]) in the data sheet where this specific brother had an hours submission
        index = np.where(arr == bro)[0]

        # arr[index, 1] is another python slicing operation that returns a list of the first value in each index of the array above
        # basically (if we pretend index is the list of indices above) it's the same thing as [ arr[0][1] , arr[4][1], arr[127][1], ...]
        # we want that [1] element cause that's the hour submission
        # and then we can sum over it really easily
        hours = arr[index, 1].sum()

        # log brothers ba number and their hours sum in that empty array we made
        # in hindsight, a Python dictionary would've made more logical sense, but at the same time,
        # a np array can save to an excel spreadsheet, which makes formatting and sharing the hours totals easier later
        brothers_sum[i][0] = bro
        brothers_sum[i][1] = hours

        i += 1

    # Save totals to a .csv (comma separated values file)
    # Can load this file into excel using "insert data > csv/file" (or something like that)
    np.savetxt("totals.csv", brothers_sum, delimiter=",")


# the __main__ thing is honestly unnecessary.
# I had initally thought I was going to make multiple .py files for this project (which is where this would come in handy),
# .. but I didn't so it's stupid, but whatever..
if __name__ == "__main__":
    read_in()
