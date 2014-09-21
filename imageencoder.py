# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Moriya Shrine"
__date__ ="$Aug 23, 2014 11:19:56 PM$"
import myEncoder
import os
url = 'http://perso.wanadoo.es/larigon2/fotos/charmander.bmp'
pageUrl = 'http://perso.wanadoo.es/larigon2/fotos/charmander.bmp'
#myEncoder.encodeMessageInBitmap()
#myEncoder.decodeMessageFromBitmap()

#myEncoder.encodeMessageInBitmap('Hello World :D')
#myEncoder.decodeMessageFromBitmap()

#message = input('Secret Message: ')
#imageName = input('Image Name: ')
#myEncoder.encodeMessageInBitmap(message,imageName)
#myEncoder.decodeMessageFromBitmap(imageName + "2")

#myEncoder.encodeMessageInBitmapFromUrl(url)
#myEncoder.decodeMessageFromBitmap('dlImage2')
myEncoder.getImageLocation(pageUrl)
print('end')


