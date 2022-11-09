import cv2
import numpy as np
import os
import json

if 'IMAGE_PATH' in os.environ:
  metadata = json.loads(os.environ['DATA'])
  properties = json.loads(metadata['properties'])
  annotations = json.loads(metadata['annotations'])
  for image_filename in os.environ['IMAGE_PATH'].split(','):
    image = cv2.imread(image_filename)
    ret, image = cv2.threshold(image,properties['threshold'],255,cv2.THRESH_BINARY)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    off = 0
    all = 0
    result_annotations = []
    for annotation in annotations['annotations']['light-source']:
      all += 1
      if np.average(gray[annotation['y']:annotation['y']+annotation['h'], annotation['x']:annotation['x']+annotation['w']]) < properties['threshold']:
        off += 1
        annotation['result'] = 'off'
      else:
        annotation['result'] = 'on'
      result_annotations.append(annotation)
    print(json.dumps({
      'Field': {
        'Off': off,
        'All': all
      },
      'Property': {
        'CameraID': metadata['cameraID']
      },
      'Result': json.dumps({
        'regions': result_annotations
      })
    }))
if 'STREAM_URL' in os.environ:
  metadata = json.loads(os.environ['DATA'])
  properties = json.loads(metadata['properties'])
  annotations = json.loads(metadata['annotations'])
  vcap = cv2.VideoCapture(os.environ['STREAM_URL'], cv2.CAP_FFMPEG)
  while(True):
    ret, image = vcap.read()
    if ret:
      ret, image = cv2.threshold(image,properties['threshold'],255,cv2.THRESH_BINARY)
      gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      off = 0
      all = 0
      result_annotations = []
      for annotation in annotations['annotations']['light-source']:
        all += 1
        if np.average(gray[annotation['y']:annotation['y']+annotation['h'], annotation['x']:annotation['x']+annotation['w']]) < properties['threshold']:
          off += 1
          annotation['result'] = 'off'
        else:
          annotation['result'] = 'on'
        result_annotations.append(annotation)
      print(json.dumps({
        'Field': {
          'Off': off,
          'All': all
        },
        'Property': {
          'CameraID': metadata['cameraID']
        },
        'Result': json.dumps({
          'regions': result_annotations
        })
      }))