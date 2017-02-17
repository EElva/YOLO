import tinyCore
import argparse
import tkinter
from PIL import Image
import numpy as np

def processImage():
    if ( fileSource == "cam" ):
       response = requests.get(  "http://192.168.0." + stationNo + "/image.jpg" )
       file = BytesIO( response.content )
       img = Image.open( file )
       img = img.resize( ( 240, 320 ) )
    else:
       img = Image.open( fileSource )

    pilImage = img.convert( 'L' )

    yolo.jimg = img

    yolo.detect_from_cvmat( np.array( img ) )


def eventLoop():
    processImage()
    if ( fileSource == "cam" ):
       root.after( 100, eventLoop )
	
parser = argparse.ArgumentParser()

parser.add_argument("-image",
                    help="jpg file containing image for recognition")

parser.add_argument("-stationNo",
                    help="jpg file containing image for recognition")
args = parser.parse_args()

fileSource = args.image
stationNo = args.stationNo

yolo = tinyCore.YOLO_TF()
yolo.build_networks()
#yolo.detect_from_cvmat( args.image )

root = tkinter.Tk()
#root.geometry( '%dx%d' % (240,320) )
root.geometry( '%dx%d' % (640,360) )
yolo.label_image = tkinter.Canvas( root )

eventLoop()

root.mainloop()
