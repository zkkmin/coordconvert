Coordinate Converter For SVY21 and WGS84
========================================

A Python script to convert coordinates to and from 3414 SVY21 Singapore to 4326 WGS84. 

This script uses 'http://tasks.arcgisonline.com/ArcGIS/rest/services/Geometry/GeometryServer/project'
service for conversion.


Input CSV File
--------------
*	Input file must be a cvs file with 2 columns heading X and Y or Lat and Lng.

*	The output file will contain original two columns and two result columns.

*	To convert WGS to SVY, use WGS2SVY as third argument.

*	To convert SVY to WGS, use SVY2WGS as third argument.


Usage
-----
*	To convert from WGS84 to SVY21

	```
	coordConverter.py INPUT_FILE.csv OUTPUT_FILE.csv WGS2SVY
	```
*	To convert from SVY21 to WGS84

	```
	coordConverter.py INPUT_FILE.csv OUTPUT_FILE.csv SVY2WGS
	```