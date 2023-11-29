import arcpy
import os

gdp_path = r"C:\Users\shiva\Downloads\ProProject_Cursors\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdp_path,fc_name)

field_list = ["NAME","ESTAB","ADDR","CITYNM","ZIP","EMP","ACRES"]

record= ("New Town Restaurant",2021,"841 STREET","SAN DIEGO",92101,150,10)

i_cursor = arcpy.da.InsertCursor(fc_path,field_list)
i_cursor.insertRow(record)

