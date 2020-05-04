# -*- coding: utf-8 -*-
# Name: Clip_Example2.py
# Description: Clip major roads that fall within the study area. 

# Import system modules
import arcpy

# Set local variables
in_features = r"D:\PythonTry\Cliptest.gdb\Ilan_polyline_1"
clip_features = r"D:\PythonTry\Polygon_2.shp"
out_features = r"D:\PythonTry\Cliptest\cliptry_3.shp"


# Execute Clip
arcpy.Clip_analysis (in_features, clip_features, out_features)

print "Finished."
