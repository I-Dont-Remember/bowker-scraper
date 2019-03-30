import xlsxwriter
import os.path
import datetime
from subjects import subject_list

# create unique filename such as bowker_scraper_30_Mar_2019_000.xlsx
count = 0
date = datetime.datetime.now()
workbookName = "bowker_scraper_" + str(date.day) + "_" + date.strftime("%b") + "_" + str(date.year) + "_" + "%03d" % (count) + ".xlsx"
while os.path.isfile(workbookName) and count < 1000:
    count = count + 1
    workbookName = "bowker_scraper_" + str(date.day) + "_" + date.strftime("%b") + "_" + str(date.year) + "_" + "%03d" % (count) + ".xlsx"
if (count >= 1000):
    print "Could not create unique filename. Exiting..."
    exit(0)

# open new Excel workbook and make percentages sheet
print workbookName
workbook  = xlsxwriter.Workbook(workbookName)
worksheet = workbook.add_worksheet("Percentages")
bold = workbook.add_format({'bold': True})

# row is amount of years the data is for, starting in 1957 + 1 for year row
# col is amount of subjects + 2 for subject name row
for row in range(63):
    for col in range(len(subject_list)+1):
        # set up years
        if col == 0:
            if row == 0:
                worksheet.write(row, col, "Year", bold)
            else:
                worksheet.write(row, col, row+1956, bold)
        # write subject name in top row of each col, then data underneath
        else:
            if row == 0:
                worksheet.write(row, col, subject_list[col-1], bold)
            else:
                # TODO: get amount of books DATA_NUMBER
                DATA_NUMBER = 1
                worksheet.write(row, col, DATA_NUMBER)

workbook.close()
print "Done with data collection."
