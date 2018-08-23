#create_richness_map.py
#Created by Ruben Dario Palacio
#with valuable contributions by John Fay.
#Nicholas School of the Environment
#Duke University, NC, USA. 
#December 2017

import sys, os, arcpy
from arcpy import sa, env

# Check out the ArcGIS Spatial Analyst
arcpy.CheckOutExtension("Spatial")

#Allow to overwrite files
arcpy.env.overwriteOutput = True

#Get relative paths            
scriptWS = os.path.basename(sys.argv[0]) 
rootWS = os.path.dirname(sys.path[0])   
dataWS = os.path.join(rootWS,"Data")    
tempWS = os.path.join(rootWS,"Scratch")

#Set Environmental Variables
arcpy.env.workspace = tempWS + "\\surp_ind_rast\\raster_reclass"

# Set Mask environment
arcpy.env.mask = dataWS + "\\snap_raster1.img"

#Get rasters
rasters = arcpy.ListRasters()
print rasters

# Execute cell statistics
out_raster = sa.CellStatistics(rasters, statistics_type = "SUM")
out_raster.save(tempWS + "\\richness_map\\richness1.img")

print "Done!"

    
    
   
    

	








