import pandas
import arcpy
import os

csv_path = r"C:\Users\shiva\Documents\programming_iii\P5_working_with_cursors_2\estab_years.csv"
year_dict = {}
csv_df = pandas.read_csv(csv_path)

for index,row in csv_df.iterrows():
    year_dict[row.NAME] = row.ESTAB
#print(year_dict)

gdp_path = r"C:\Users\shiva\Downloads\Practical_5_6_ProProject\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"
fc_path = os.path.join(gdp_path,fc_name)
field_list = ["NAME","ESTAB"]

with arcpy.da.UpdateCursor(fc_path,field_list) as u_cursor:
    for row in u_cursor:
        if row[0] in year_dict:
            row[1] = year_dict[row[0]]
        else:
            print("{} is not in majorAttraction file".format(row[0]))
        u_cursor.updateRow(row)

