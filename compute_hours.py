import numpy as np
import pandas as pd
import csv


# path = "C:\\Users\\joelb\\Desktop\\healthcare_outcomes\\data\\sandbox.xlsx"

def read_in():

    features = ['BA','Hours']
    readin = pd.read_excel('hours.xlsx')

    # Filter features and fill NaN values with -1.0
    filtered = pd.DataFrame(readin, columns=features).fillna(-1)
    arr = filtered.to_numpy().reshape(-1,2)

    brothers = np.unique(arr[:,0])
    brothers_sum = np.zeros((len(brothers),2))

    i = 0
    for bro in brothers:
        index = np.where(arr == bro)[0]
        hours = arr[index,1].sum()

        brothers_sum[i][0] = bro
        brothers_sum[i][1] = hours
        i += 1

    np.savetxt('totals.csv', brothers_sum, delimiter=',')
    
    
if __name__ == "__main__":
    read_in()
