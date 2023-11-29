import arcpy
import os
gdp_path = r"C:\Users\shiva\Downloads\ProProject_Cursors\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdp_path,fc_name)

field_list = ["NAME","ESTAB","HISTORIC"]

with arcpy.da.UpdateCursor(fc_path,field_list) as U_cursor:
    for row in U_cursor:

        if row[1]<1960:
            row[2] = "yes"
        else:
            row[2] = "No"
        U_cursor.updateRow(row)

