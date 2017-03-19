# location-quotient
ArcPy tool for calculating a Location Quotient

## But what's a Location Quotient?
The Location Quotient (LQ) is a hot spot/cold spot ratio compares a local rate to a global rate. For example, the percentage of foreign born population in Maryland is about 14%. However, if you look at the the percentage of foreign born by census tract, it varies from 0% to 75%. A census tract with 7% of its population being foreign born would have an LQ value of 0.5 indicating that in this local geography has a rate of foreign born population half that of the global rate (dispersion of foreign born population). If a census tract had an LQ value of 2, that would indicate that the census tract has a foreign born population rate twice that of the global rate (concentration of foreign born population).


## What each file is:
`Location_Quotient_Calculator.py` contains the code with comments

`Location_Quotient_Calculator_Min.py` contains the code without comments

`Location_Quotient_Calculator_Min_Param.py` is the basis for the code

## What the tool box is:
AlexTools.tbx contains the location quotient code as a script tool. This tool has worked in initial testing on my machine but is still being debugged for use for others

## What the sample data geodatabase has:
Sample_Data.gdb is a geodatabase of Maryland ACS tracts with population counts and foreign born population counts

## How to use the tool:
1. Select the feature class with the fields you want to calculate
2. For Population, select the field with the counts of the overall population
3. For Sub Population, selct the group you want to calculate the location quotient for

## But you want to use it for something else
For now, in your favorite text editor, open up

>	Location_Quotient_Calculator_Min.py

1. For `feat`, replace `Maryland_Tracts` with your feature class
2. For `globalPop`, replace `Population` with the total population field in your feature class
3. For `localPop`, replace `Foreign_Born_Population` with the sub population field in your feature class that you want to calculate the location quotient for
4. Open up the Python window in ArcGIS, make sure your feature class is loaded into the MXD
5. Run
6. Inspect output (hopefully not error message!)
