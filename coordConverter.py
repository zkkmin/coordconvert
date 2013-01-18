"""
    To convert coordinates to and from '3414 SVY21_Singapore_TM' to
     4326 for WGS84. This script uses
     'http://tasks.arcgisonline.com/ArcGIS/rest/services/Geometry/GeometryServer/project'
     service for conversion.

    Input file must be a csv file with 2 columns heading X and Y or Lat and Lng.
    The output file will contain original two columns and two result columns.
    To convert WGS to SVY, use WGS2SVY as third argument.
    To convert SVY to WGS, use SVY2WGS as third argument.
     
"""

import urllib2
import csv
from sys import argv
import sys

# If python version is 2.5, install simplejson module and modified the module path in sys.path.apped()
if sys.version_info[:2][1] > 5:
    import json
else:
    sys.path.append("C:\\Python25\\Lib\\site-packages\\simplejson-3.0.7-py2.5.egg")
    import simplejson as json

if len(argv) < 4:
    print ("Input Error.")
    print ("Usage WGS84 to SVY21 >> coordConverter.py INPUT_FILE.csv OUTPUT_FILE.csv WGS2SVY")
    print ("Usage SVY21 to WGS84 >> coordConverter.py INPUT_FILE.csv OUTPUT_FILE.csv SVY2WGS")
    exit(1)
else:
    print "Converting coordinates ... "

    infilename = argv[1]
    outfilename = argv[2]
    command = argv[3]

    infile = open( infilename )
    outfile = open (outfilename, "wb" )

    csvReader = csv.DictReader( infile )
    csvWriter = csv.writer( outfile )
    
    csvWriter.writerow( ["X", "Y", "Lat", "Lng"] )
    
    url = "http://tasks.arcgisonline.com/ArcGIS/rest/services/Geometry/GeometryServer/project?"
    inSR = ""
    outSR = ""
    X = ""
    Y = ""

    try:        
        for row in csvReader:
            if command == "WGS2SVY":
                inSR = "4326"
                outSR = "3414"
                X = row["Lng"]
                Y = row["Lat"]
            elif command == "SVY2WGS":
                inSR = "3414"
                outSR = "4326"
                X = row["X"]
                Y = row["Y"]
            else:
                print "Error, command should be either 'WGS2SVY' or 'SVY2WGS'."
                break
            
            geometries = 'geometries=%7B"geometryType"%3A"esriGeometryPoint"%2C"geometries"%3A%5B%7B"x"%3A' + X + '%2C"y"%3A' + Y + '%7D%5D%7D&f=pjson'  
            fullurl = url + 'inSR=' + inSR + '&outSR=' +outSR + '&' + geometries
            request = urllib2.Request(fullurl)
            contents = json.load(urllib2.urlopen(request))

            Xout = contents['geometries'][0]['x']
            Yout = contents['geometries'][0]['y']

            if command == "WGS2SVY":
                outrow = [ Xout, Yout, Y, X ]
            else:
                outrow = [ X, Y, Yout, Xout ]
                
            csvWriter.writerow(outrow)
    except Exception:
        print "Error : " , sys.exc_info()[0]
    finally:
        infile.close()
        outfile.close()



















        
    
