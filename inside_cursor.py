# update the value to 1998 of ESTAB if the existing value is 0 using udate cursor
import arcpy
import os

gdp_path = r"C:\Users\shiva\Downloads\Practical_5_6_ProProject\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdp_path,fc_name)

field_list = ["NAME","ESTAB","ADDR"]

record_0 = ("NewAttraction",2023,"Street123")

record_list =[("NewAttraction_1",2023,"Street124"),("NewAttraction_2",2023,"Street125"),("NewAttraction_3",2023,"Street128")]


i_cursor = arcpy.da.InsertCursor(fc_path,field_list)

for record in record_list:
    i_cursor.insertRow(record)

