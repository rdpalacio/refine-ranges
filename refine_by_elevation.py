#refine_by_elevation.py
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
arcpy.env.workspace = dataWS

# Creates a Raster Object from the DEM
dem = arcpy.Raster("dem.img")

# Specify the feature class with the ranges of birds 
birds = "birds.shp"

# Create a cursor
rows = arcpy.SearchCursor(birds)

for ranges in rows:
    spp = ranges.getValue("SCINAME")         #Get the scientific name found in the attribute table
    min_elev = ranges.getValue("MIN_ELE")    #Get the minimum elevation found in the attribute table  
    max_elev = ranges.getValue("MAX_ELE")    #Get the maximum elevation found in the attribute table 
    print spp, min_elev, max_elev
    spp_raster = arcpy.Raster(os.path.join(tempWS + "\\rasters", spp + ".img"))     #Get the spp raster
    arcpy.env.mask = spp_raster                                                     #Use it as a mask
    out_raster = sa.Con(((dem > min_elev) & (dem < max_elev)),1)                  #Refine by elevation
    out_raster.save((tempWS + "//rasters_elev//{}.img").format(spp))           #Save the refined range to scratch folder
    
print "Done!"

    
    
   
    

	








