All processed data is located in the 'data/' folder of this repository.

If you wish to download your own kelp canopy and SST data for different sites, follow the instructions below:

**Downloading kelp canopy cover data:**

All kelp canopy area data was downloaded from kelpwatch.org. Navigate to your site of interest and define a border around the site by drawing a polygon or rectangle. Download the .csv file from the website into your project folder. 

**Importing and processing SST data:**

Sea surface temperature (SST) for this project was downloaded from the PODAAC website (https://podaac.jpl.nasa.gov/GHRSST?tab=mission- objectives&sections=about%2Bdata). The data downloaded was from the GHRSST Level 4 MUR Global Foundation Sea Surface Temperature Analysis (v4.1), shortname MUR-JPL-L4-GLOB-v4.1.

The code for downloading was derived from https://github.com/podaac/data-subscriber/tree/main.

This code is provided in the 'SST_download' notebook if the user would like to download their own SST data for different dates or using a different satellite. 

Also provided in the 'SST_download' notebook are instructions for gathering SST for your defined kelp canopy sites. Follow the code by inputting the coordinates for the site you downloaded kelp canopy area for. 

These site boundaries can then be used to create annual average winter SST for each site, which can be exported as a .csv to your project folder. 

