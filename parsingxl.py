#Parses excel file with results from biek.edu.pk to calculate number of students with Above 70% and 80%
import openpyxl,re
wb = openpyxl.load_workbook('result.xlsx') #importing the excel sheet

sheet = wb.get_active_sheet() #making a sheet object

mo = re.compile("\d{6}\((\d\d\d)\+?\^?\s?(\d?)\)") #making the regex to catch rollnumbers from the cells
total=[]
aboveseventy=[]
aboveeighty=[]
rows=sheet.rows #row iterator

for row in rows:
    for cell in row: #cycling through rows and cells
        sto=mo.match(str(cell.value)) #matching the value of each cell with the regex to see if we've caught a proper roll number
        if sto is not None:
            num=int(sto[1])
            if sto[2]: #if bonus marks were awarded adding them to the original num
                num += int(sto[2])
            total.append(num)
            percentage=(num/1100)*100
            print(cell.value)
            if percentage >= 70:
                aboveseventy.append(num)
            if percentage >= 80:
                aboveeighty.append(num)
        else:
            print(cell.value)

print("Ratio of students above 70%: {}".format((len(aboveseventy)/len(total))*100)
     + "\nRatio of students above 80%: {}".format((len(aboveeighty)/len(total))*100)
      +"\nNumber of students above 70%: {}".format(len(aboveseventy))
      +"\nNumber of students above 80%: {}".format(len(aboveeighty))
      +"\nTotal number of students passed: {}".format(len(total)))


