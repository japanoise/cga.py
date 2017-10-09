#!/usr/bin/python
import sys
import os

import PIL
from PIL import Image

PALETTE = [
    0,   0,   0,    # black,  00
    85,  255, 255, # cyan,  01
    255, 85,  255,    # red,    10
    255, 255, 255,  # white, 11
] + [0, ] * 252 * 3

# a palette image to use for quant
pimage = Image.new("P", (1, 1), 0)
pimage.putpalette(PALETTE)

for imgfn in sys.argv[1:]:
    # open the source image
    image = Image.open(imgfn)
    image = image.convert("RGB")
    # quantize it using our palette image
    imagep = image.quantize(palette=pimage)
    # get new filename
    dirname, filename= os.path.split(imgfn)
    name, ext= os.path.splitext(filename)
    newpathname= os.path.join(dirname, "cga-%s.png" % name)
    # save
    imagep.save(newpathname)
