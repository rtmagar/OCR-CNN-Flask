# OCR-CNN-Flask


The project consists of a model trained to extract words from natural scene images. When the users upload images, the detector will preprocess and crop the detect words from the images and saves it for classification. The classifier will then predict the word with highest confidence and return (*) if the word is not in the dictionary.

## Requirements
* OpenCV
* Tesseract
* Tessorocr
* Keras
* Numpy
* Pillow
* Tensorflow 
* Flask

