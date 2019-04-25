# ImageShredder
Shredding an image with an RNG seeded with the hash of a given password

Command line interface written in python


Usage:

Shredded strips with predictable randomization
  > $ ./shredde.py needShredding.jpg

Shredded strips of original image will be randomized using the key as a seed
  > $ ./shredder.py needShredding.jpg -o shredded.jpg -e -k hunter2

Input a shredded image from above using same key to get back original image
  > $ ./shredder.py shredded.jpg -o unshredded.jpg -d -k hunter2


