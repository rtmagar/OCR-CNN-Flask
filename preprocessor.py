from PIL import Image
from tesserocr import PyTessBaseAPI, RIL
import numpy
import argparse
import csv
import cv2
import os
import classifier

def detector(image):
  # load the example image and convert it to grayscale
  inputImage = cv2.imread(image)
  gray = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
  # Threshold the image
  gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

  # Write the grayscale to temp file
  filename = "{}.png".format(os.getpid())
  cv2.imwrite(filename, gray)

  with PyTessBaseAPI() as api:
    # Send the new grayscale image into Tesseract
    api.SetImageFile(filename)

    # We will segment the grayscale by words
    boxes = api.GetComponentImages(RIL.WORD, True)

    # With each bouding box for the words
    for i, (im, box, _, _) in enumerate(boxes):
      # Grab the coordinates of the bounding box
      api.SetRectangle(box['x'], box['y'], box['w'], box['h'])

      # Turn the returned bounding box coordinates into an array of coordinates
      coord = list(box.values())

      # Load grayscale for cropping
      cropper = Image.open(filename)

      # Cropped image is saved into new variable
      crop_image = cropper.crop(
        (coord[0],
        coord[1],
        coord[0]+coord[2],
        coord[1]+coord[3])
      )

      # Convert the new image into a numpy array
      cropped = numpy.array(crop_image) 

      # Create the new file name for the word
      word_file = "word_" + str(i) + ".png"

      # Have OpenCV save the cropped image into the new file
      cv2.imwrite(word_file, cropped)

  # Remove the grayscale image
  os.remove(filename)


