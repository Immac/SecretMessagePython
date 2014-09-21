
__author__="Moriya Shrine"
__date__ ="$Aug 23, 2014 11:25:29 PM$"

import itertools
import os
from sys import exit
import urllib.request
from bs4 import BeautifulSoup
import asdf
def encodeMessageInBitmap(message = 'Be sure to drink your ovaltine!',imageName = 'image'):  
    bitmapExtension = '.bmp'
    byteToSkip = 64   
    output = []
    lastChar = chr(255)
    message += lastChar
    if bitmapExtension in imageName:
        imageName.replace(bitmapExtension, '')
    inputImageName = imageName + bitmapExtension
    outputImageName = imageName + str(2) + bitmapExtension
    charList = list(message)
    intList = list(ord(x) for x in charList)
    numlist = list([int(x) for x in list('{0:0b}'.format(num))] for num in intList)
    #print(numlist)
    for element in numlist:
        while len(element) < 8:
            element.insert(0, 0)
    mergedNumList = list(itertools.chain(*numlist))
    size = os.path.getsize(inputImageName) - byteToSkip
    sizeNeeded = len(mergedNumList)
    if size < sizeNeeded:
        print(kNotEnoughSpace)
        exit()
    #print(size)
    #print(sizeNeeded)
    #print(binaryList)
    #print(mergedNumList)
    #print(numlist)
    with open(inputImageName, "rb") as imageFile:
        for i in range(0, byteToSkip):
            output.append(ord(imageFile.read(1)))
        byte = imageFile.read(1)
        for item in mergedNumList:
            newByte = ((ord(byte) & ~1) | item)
            #print(newByte)
            output.append(newByte)
            byte = imageFile.read(1)
        while byte:
            #print(byte)
            output.append(ord(byte))
            byte = imageFile.read(1)
    with open(outputImageName, "wb") as imageFile:
        #print(output)
        newByteArray = bytes(output)
        #print(newByteArray)
        imageFile.write(newByteArray)

def decodeMessageFromBitmap(imageName = 'image2',bitmapExtension = '.bmp'):
    bytesToSkip = 64
    #processing
    inputImageName = imageName + bitmapExtension
    with open(inputImageName, "rb") as imageFile:
        imageFile.read(bytesToSkip)
        byteArray = []
        byte = imageFile.read(1)
        while byte:
            byteArray.append((ord(byte)))
            byte = imageFile.read(1)
    outputList = []
    outputListItem = ""
    counter = 0
    #print(byteArray)
    #os.system('pause')
    for item in byteArray:
        num = str(item % 2)
        outputListItem += num
        counter += 1
        if counter % 8 == 0:
            outputList.append(int(outputListItem, 2))
            outputListItem = ""
    charList = []
    for x in outputList:
        if x > 128:
            break
        charList.append(chr(x))
    mergedCharList = ''.join(charList)
    return mergedCharList
    
    

def getImageLocation(url,message = 'Be sure to drink your ovaltine!', imageName = "dlImage"):
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html);
        all_links = soup.find_all('a');
        all_images = soup.find_all('img');
        foundCounter = 0;
        for link in all_links:
            imgUrl = link["href"]
            if imgUrl.endswith('.bmp'):
                foundCounter += 1;
                imgNewName = imageName + str(foundCounter);
                #encodeMessageInBitmapFromUrl(imgUrl,message, imageNewName)
                print(imgNewName)
        for img in all_images:
            imgUrl = img["src"]
            if imgUrl.endswith('.bmp'):
                foundCounter += 1;
                imgNewName = imageName + str(foundCounter);
                #encodeMessageInBitmapFromUrl(imgUrl,message, imageNewName)
                print(imgNewName)
        return html


def encodeMessageInBitmapFromUrl(url,message = 'Be sure to drink your ovaltine!', imageName = "dlImage"):
    bitmapExtension = '.bmp'
    if(url == ''):
        exit('empty url!')
    urllib.request.urlretrieve(url, imageName + bitmapExtension)
    
    encodeMessageInBitmap(message,imageName)
