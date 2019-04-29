# ImageShredder
Shredding a PNG or BMP image with an RNG seeded with the hash of a given password

Command line interface written in python


Usage:

Shredded strips with predictable randomization
  > $ ./shredder.py needShredding.png

Shredded strips of original image will be randomized using the key as a seed
  > $ ./shredder.py needShredding.png -o shredded.png -e -k hunter2

Input a shredded image from above using same key to get back original image
  > $ ./shredder.py shredded.png -o unshredded.png -d -k hunter2

NOTE: Does not work with JPEG images, I believe, due to it's compression when saving and reopening. Will work on a fix for that.



