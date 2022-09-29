import cv2
import numpy as np
import os
import json

if 'IMAGE_PATH' in os.environ:
  for image_filename in os.environ['IMAGE_PATH'].split(','):
    frame = cv2.imread(image_filename)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = hog.detectMultiScale(frame, winStride=(8, 8),
      padding=(16, 16), scale=1.05)
    print(json.dumps({
      'Field': {
        'Numbers': len(rects.tolist()) if rects.__class__.__name__ == 'ndarray' else len(rects)
      },
      'Property': {
        'ImagePath': image_filename
      },
      'Result': json.dumps({
        'rects': rects.tolist() if rects.__class__.__name__ == 'ndarray' else rects,
        'weights': weights.tolist() if weights.__class__.__name__ == 'ndarray' else weights
      })
    }))