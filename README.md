# location-quotient
Script written using Python and ArcPy for calculating a Location Quotient


## But what's a Location Quotient?
The Location Quotient (LQ) is a hot spot/cold spot ratio compares a local rate to a global rate. For example, the percentage of foreign born population in Maryland is about 14%. However, if you look at the the percentage of foreign born by census tract, it varies from 0% to 75%. A census tract with 7% of its population being foreign born would have an LQ value of 0.5 indicating that in this local geography has a rate of foreign born population half that of the global rate (dispersion of foreign born population). If a census tract had an LQ value of 2, that would indicate that the census tract has a foreign born population rate twice that of the global rate (concentration of foreign born population).


## I'm coming from your website which used Hispanic population as example
That's ok! I wrote the script at a different time than when I did the original web page. I wanted to test it out with different data. Substitute in any local population and global population that you like.


## How to use the script:
1. Set up your MXD with the data that you want to analyze
2. Pull up the script in your favorite text editor
3. Change the 'feat' variable to your project geography that contains the data
4. Change 'globalPop' to the overall population of your analysis
5. Change 'localPop' to the local population of your analysis
6. Copy paste into the Python window of your ArcGIS session and run the script


## System requirements
This tool was written for ArcGIS 10.1 and above. The tool may work in ArcGIS Pro or ArcGIS 10.0 and below but has not been tested in either.
