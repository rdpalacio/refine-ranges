#refine_by_habitat.py
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
arcpy.env.workspace = tempWS + "\\rasters_elev"

# Creates a Raster Object from the forest cover for map algebra calculations
habitat = arcpy.Raster(dataWS + "\\forest_cover.img")

#Get rasters refined by elevation
rasters = arcpy.ListRasters()
print rasters


#Refine ranges by habitat
for in_raster in rasters:
    mask_raster = arcpy.Raster(in_raster)
    arcpy.env.mask = mask_raster
    out_raster = sa.Con(habitat == 1,1,0)                       #Refine by habitat
    out_raster.save((tempWS + "\\rasters_hab\\" + in_raster))    #Save the refined range to scratch folder
    
print "Done!"

    
    
   
    

	








