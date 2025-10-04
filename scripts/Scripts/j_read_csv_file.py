'''
Reads a csv into a list of all of the rows and returns the list of rows
Example usage: my_rows = j_read_csv("CelestialData.csv") my_rows has the contents of the csv
'''
import csv
def j_read_csv(filename):
    name, url, ra, dec, text1, text2, text3 = [], [], [], [],[], [], []
    rows = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            name.append(row[0])
            url.append(row[1])
            ra.append(row[2])
            dec.append(row[3])
            text1.append(row[4])
            text2.append(row[5])
            text3.append(row[6])
            rows.append(row)
    return rows