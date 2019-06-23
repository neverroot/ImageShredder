#!/usr/bin/env python3

import sys
import random
import argparse
import hashlib
from PIL import Image


def encrypt(seed,img):
    #seeds with hash of password given by user
    random.seed(seed,2)

    #creates list filled with strips of image of width 1p
    imglist = [img.crop((i,0,i+1,img.height)) for i in range(img.width)]
    corresponding = list(range(img.width))
    indicies = []
    #create random list of non-repeating numbers from [0:image_height]
    while(len(corresponding)!=0):
        randVal = random.randint(0,len(corresponding)-1)
        indicies.append(corresponding[randVal])
        del corresponding[randVal]
    #uses random numbers to correspond to index of the list of image strips
    shuffled = []
    for i in indicies:
        shuffled.append(imglist[i])

    return shuffled


def decrypt(seed,img):
    #seeds with hash of password given by user
    random.seed(seed,2)
    #creates list filled with strips of image of width 1p
    imglist = [img.crop((i,0,i+1,img.height)) for i in range(img.width)]
    unshuffled = list(range(len(imglist)))
    corresponding = list(range(len(imglist)))
    indicies = []
    #create same random list of non-repeating numbers from [0:image_height]
    while(len(corresponding)!=0):
        randVal = random.randint(0,len(corresponding)-1)
        indicies.append(corresponding[randVal])
        del corresponding[randVal]
    counter = 0
    #corresponds the random numbers to index of the list of image strips
    for i in indicies:
        unshuffled[i] = imglist[counter]
        counter+=1
    return unshuffled

def main(args):
    #checks if image exists
    imgpath = args.imagepath   
    try:
        img = Image.open(imgpath)
        img.show()
    except FileNotFoundError:
        print('This file path does not exist. Try again')
        sys.exit(0)

    #gets important image data
    height = img.height
    width = img.width
    mode = img.mode

    #checks for user just wanting a quick "random" shred
    if(not args.encrypt and not args.decrypt):
        canv = Image.new(mode,(width,height))
        plainshred = [img.crop((i,0,i+1,height)) for i in range(width)]
        random.shuffle(plainshred)
        counter=0
        for images in plainshred:
            canv.paste(images,(counter,0,counter+1,height))
            counter+=1
        canv.save(args.output_file)
        canv.show()
        sys.exit(0)

    imglist = []

    if(args.encrypt):
        k = ''
        if(args.key):
            k = args.key
        else:
            k = input("Enter key: ")
        
        hash_object = hashlib.sha1(k.encode('ascii'))
        seed = hash_object.hexdigest()
        print("encrypt seed: " + seed)
        imglist = encrypt(seed,img)
    
    if(args.decrypt):
        k = ''
        if(args.key):
            k = args.key
        else:
            k = input("Enter key: ")
        
        hash_object = hashlib.sha1(k.encode('ascii'))
        seed = hash_object.hexdigest()
        print("decrypt seed: " + seed)
        imglist = decrypt(seed,img)

    #create canvas and fills it with strips
    canvas = Image.new(mode,(width,height))
    counter = 0
    for images in imglist:
        canvas.paste(images,(counter,0,counter+1,height))
        counter+=1
    canvas.save(args.output_file)
    canvas.show()

    
    if args.output_file != 'shredder_output.png':
        print('Image saved to ' + args.output_file)


if __name__ == "__main__":
    #Parses positional and conditional arguments for shredder module
    parser = argparse.ArgumentParser()
    parser.add_argument('imagepath', help='Path of image')
    parser.add_argument('-o', '--output-file',metavar='',default='shredder_output.jpg',help='path of output file',)
    parser.add_argument('-k', '--key',metavar='',help='key used to encrypt or decrypt')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d','--decrypt',action='store_true',help='decrypts shredded image')
    group.add_argument('-e','--encrypt',action='store_true',help='encrypts given image')
    args = parser.parse_args()
    print(args)
    #pass all arguments to main function
    main(args)
