import arcpy


# EDIT THE FOLLOWING LINES ### 
############################
arcpy.env.workspace="G:/Rathore/vic_auto6"                  ### Put a folder location (a new folder is suggested)
basin="G:\\ARORA\\India_SHP\\INDIA.shp"                 ### Location of shapefile of basin for which soil map will be generated  (in GCS_WGS_1984)

hwsd_excel='G:\\Rathore\\HWSD_RASTER\\HWSD_CLS_DATA.xlsx'   ### Location of hwsd_class data excel file, provided with this code
text_class='G:\\Rathore\\HWSD_RASTER\\text_class.xlsx'      ### Location of text_class data excel file, provided with this code
hwsd="G:\\Rathore\\HWSD_RASTER\\hwsd.bil"                   ### Location of hwsl.bil file, provided with this code
###############################################################################################################

#  DO NOT  EDIT FROM  HERE
arcpy.env.overwriteOutput=True


out=arcpy.sa.ExtractByMask(hwsd,basin)
out.save("hwsd_ext")

arcpy.ExcelToTable_conversion(hwsd_excel,"hwsd_tab")
arcpy.JoinField_management("hwsd_ext","VALUE","hwsd_tab","MU_GLOBAL")
out_re=arcpy.sa.Reclassify("hwsd_ext","T_USDA_TEX",arcpy.sa.RemapValue([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11],[12,12],[13,13]]))
out_re.save("soil_fao")
arcpy.ExcelToTable_conversion(text_class,"text_class_tab2")
arcpy.JoinField_management("soil_fao1","VALUE","text_class_tab2","CODE")

print "A soil map for the given basin area has been perpared with the name soil_fao in the workspace"