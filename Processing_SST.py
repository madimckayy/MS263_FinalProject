def Importing_SST_Data(download_folder, start_date, end_date, collection= 'MUR25-JPL-L4-GLOB-v04.2'):
    """ 
    
    Function to import SST data from the Physical Oceanography Distributed Active Archive Center (PODAAC) 
    
    Parameters
    ----------
    download_folder : string
        The full directory to the file folder you want data to be downloaded to
        Example format for PC: 'C:\\Users\\maddi\\Desktop\\MS263\\Homework5\\hw5-madimckayy-main\\SST Test Download'

    start_date: string
        Starting date and time you want to download SST for
        Must be in this format: '2017-06-01T00:00:00Z'

    end_date: string
        Ending date and time you want to download SST for
        Must be in this format: '2017-06-03T00:00:00Z'

    collection: string
        (optional)
        Collection of SST data you wish to download from
        Default is MUR25-JPL-L4-GLOB-v04.2
        
    Returns
    -------
    Download Complete : string
        Prints the following statement once download is complete

    Note: To work with netCDF files in Python, you need to install a library specifically designed to
    open them. Open up the terminal you use for Anaconda and activate your preferred environment.
    Then, run the following commands:
    
    conda install netcdf4
    pip install podaac-data-subscriber

    """
    import requests
    import os
    from subscriber import podaac_data_downloader as pdd
    from subscriber import podaac_access as pa
    import argparse


    data_path = download_folder

    short_name = collection
    #another option - SMAP SSS: SMAP_JPL_L3_SSS_CAP_MONTHLY_V5
    
    start_date_time = start_date
    
    end_date_time = end_date
    
    parser = pdd.create_parser()
    args = parser.parse_args(['-c',short_name, '-d',data_path,
                              '-sd',start_date_time, '-ed',end_date_time])
    
    pdd.run(args)

    return('Download Complete')


def SST_grid(download_folder, file_name, x_min, x_max, y_min, y_max):
    """ 
    
    Function to create a defined grid with coordinates from downloaded SST 

    Parameters
    ----------
    download_folder : string
        The full directory to the file folder you downloaded SST data into
        Example format for PC: 'C:\\Users\\maddi\\Desktop\\MS263\\Homework5\\hw5-madimckayy-main\\SST Test Download'
        Note: Mac might only need one forward slash instead of two backslash's

    file_name: string
        Name of one of the files in the dowloaded folder
        Must include '.nc'. Example: '20020902090000-JPL-L4_GHRSST-SSTfnd-MUR25-GLOB-v02.0-fv04.2.nc'

    x_min: float
        Minimum horizontal (x) coordinate to define the grid (minimum longitude in decimal degrees)
        Example: -123.7
        
    x_max: float
        Maximum horizontal (x) coordinate to define the grid (maximum longitude in decimal degrees)
        Example: -123.4
    
    y_min: float
        minimum vertical (y) coordinate to define the grid (minimum latitude in decimal degrees)
        Example: 38.4
    
    y_max: float
        minimum vertical (y) coordinate to define the grid (maximum latitude in decimal degrees)
        Example: 38.6

    Returns
    -------
    sst_grid : array
        Array of SST values in the defined grid

    """
    import netCDF4 as nc4
    import numpy as np
    
    os = input('Are you a Mac or Linux user? Y/N')
    if os.lower()=='y':
        file_folder = download_folder
        file_path = file_folder + '/' + file_name

    else:
        file_folder = download_folder
        file_path = file_folder + '\\' + file_name

    ds = nc4.Dataset(file_path)
    sst_grid = ds.variables['analysed_sst']
    sst_grid = np.array(sst_grid)
    ds.close()

    min_x = x_min
    max_x = x_max
    min_y = y_min
    max_y = y_max
    
    ds = nc4.Dataset(file_path)
    x_grid = ds.variables['lon']
    x_grid = np.array(x_grid)
    y_grid = ds.variables['lat']
    y_grid = np.array(y_grid)
    sst_grid = ds.variables['analysed_sst']
    sst_grid = np.array(sst_grid)
    ds.close()
    
    min_x_index = np.argmin(np.abs(min_x - x_grid))
    max_x_index = np.argmin(np.abs(max_x - x_grid))
    
    min_y_index = np.argmin(np.abs(min_y - y_grid))
    max_y_index = np.argmin(np.abs(max_y - y_grid))

    return(sst_grid)




