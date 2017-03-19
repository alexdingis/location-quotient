## written by Alex Din
## location quotient script, initially for percentage foreign born in Maryland but has been expanded to stand alone script
## load the feature class into an mxd then run the script in the Python window, you may need to change some settings below 
## set workspace stuff
import arcpy, numpy
arcpy.env.overwriteOutput = True
## set variables
feat          = "Maryland_Tracts"         # this is the target feature class
globalPop     = "Population"              # this is the overall population
localPop      = "Foreign_Born_Population" # this is the population of interest
## set LQ field
lqField       = "LQ_%s" %(localPop)
## get the denominator
field         = arcpy.da.TableToNumPyArray(feat, globalPop, skip_nulls=True)
totalPop      = field[globalPop].sum()
field         = arcpy.da.TableToNumPyArray(feat, localPop, skip_nulls=True)
subPop        = field[localPop].sum()
lqDenominator = (float(subPop)/totalPop)
## make a new field
exists        = arcpy.ListFields(feat, lqField)
if len(exists) < 1:
	arcpy.AddField_management(feat, lqField, "DOUBLE", 6)
## calculate the field
expression    = '( ( !{0}! / !{1}! ) / {2} )'.format(localPop, globalPop, lqDenominator)
arcpy.CalculateField_management(feat, lqField, expression, "PYTHON_9.3")


