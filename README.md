# capstone
Capstone Project

```--project_config=config.json```

## Data

Nightfire V3.0 (GRAVITE)

https://eogdata.mines.edu/download_viirs_fire.html

[CSV Readme File (V30-ez):Download](https://data.ngdc.noaa.gov/instruments/remote-sensing/passive/spectrometers-radiometers/imaging/viirs/vnf/v30/vnf_readme_v30-ez_r20180828.xlsx)


Crude Oil extraction figures are published monthly, so for a given Basin there is a delay until the data is reported by the [U.S. Energy Information Administration (EIA)](https://www.eia.gov/). 
However, [Global Gas Flaring Estimates — Remotely Sensed VIIRS Nightfire Combustion](https://medium.com/@nygeog/data-focus-global-gas-flaring-estimates-remotely-sensed-viirs-nightfire-combustion-dabfa8ce2e7f?source=friends_link&sk=c2e22810974f2daca75e16613589c347) data is delivered daily from The Earth Observation Group (EOG) after it is processed from raw multispectral satellite imagery. These Gas Flaring observations can act as a proxy for understanding the production of the facilities within a given Basin. So the model would be a Regression problem with continuious data predictions for Basin Production Output using the daily data as aggregated to the Basin reported via Global Gas Flaring in the image below. 

![](https://miro.medium.com/max/1274/1*MaV1D59jA1O-gzfV-z23Qw.png)

Since production is market-depedent rather than Time-Series, this may not be exclusively a time-series analysis. Any given unit in time, may be indepedent from the time units before or after. It is the aim of this project to predict Basin Oil Production metrics using Gas Flaring Combustion data. 



https://www.eia.gov/petroleum/drilling/
https://www.eia.gov/petroleum/drilling/xls/dpr-data.xlsx

https://www.eia.gov/petroleum/drilling/xls/duc-data.xlsx


https://catalog.data.gov/dataset/tiger-line-shapefile-2017-nation-u-s-current-county-and-equivalent-national-shapefile