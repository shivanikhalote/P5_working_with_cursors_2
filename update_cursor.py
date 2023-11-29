# update the value to 1998 of ESTAB if the existing value is 0 using udate cursor
import arcpy
import os

gdp_path = r"C:\Users\shiva\Downloads\ProProject_Cursors\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdp_path,fc_name)

field_list = ["NAME","ESTAB"]

year_dict = {}
with arcpy.da.UpdateCursor(fc_path,field_list) as U_cursor:
    for row in U_cursor:
        year_dict[row[0]]=row[1]
        if row[1]==0:
            row[1]=1998
            print(row[0])
            print(row[1])
            U_cursor.updateRow(row)
    print(year_dict)
