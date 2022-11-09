from unittest import result
import aiohttp
from aiohttp import web
import cv2
import numpy as np
import json

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

async def handle(request):
  metadata = None
  filenames = []
  images = []
  rects = list()
  weights = list()
  reader = await request.multipart()
  while True:
    part = await reader.next()
    if part is None:
      break
    if part.headers[aiohttp.hdrs.CONTENT_TYPE] == 'application/json':
      metadata = await part.json()
    elif part.headers[aiohttp.hdrs.CONTENT_TYPE].startswith('image'):
      filenames.append(part.filename)
      images.append(np.asarray(bytearray(await part.read(decode=False)), dtype="uint8"))
  for image in images:
    image = cv2.imdecode(image,cv2.IMREAD_UNCHANGED)
    (rects, weights) = hog.detectMultiScale(image, winStride=(8, 8),
      padding=(16, 16), scale=1.05)
  return web.json_response({
    'Field': {
      'Numbers': len(rects.tolist()) if rects.__class__.__name__ == 'ndarray' else len(rects)
    },
    'Property': {
      'Filename': filenames
    },
    'Result': json.dumps({
      'rects': rects.tolist() if rects.__class__.__name__ == 'ndarray' else rects,
      'weights': weights.tolist() if weights.__class__.__name__ == 'ndarray' else weights
    })
  })

async def light_handle(request):
  metadata = None
  filenames = []
  images = []
  result_annotations = []
  off = 0
  all = 0
  reader = await request.multipart()
  while True:
    part = await reader.next()
    if part is None:
      break
    if part.name == 'data' or part.headers[aiohttp.hdrs.CONTENT_TYPE] == 'application/json':
      metadata = await part.json()
      properties = json.loads(metadata['properties'])
      annotations = json.loads(metadata['annotations'])
    elif part.headers[aiohttp.hdrs.CONTENT_TYPE].startswith('image'):
      filenames.append(part.filename)
      images.append(np.asarray(bytearray(await part.read(decode=False)), dtype="uint8"))
  for image in images:
    image = cv2.imdecode(image,cv2.IMREAD_UNCHANGED)
    ret, image = cv2.threshold(image,properties['threshold'],255,cv2.THRESH_BINARY)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    off = 0
    all = 0
    for annotation in annotations['annotations']['light-source']:
      all += 1
      if np.average(gray[annotation['y']:annotation['y']+annotation['h'], annotation['x']:annotation['x']+annotation['w']]) < properties['threshold']:
        off += 1
        annotation['result'] = 'off'
      else:
        annotation['result'] = 'on'
      result_annotations.append(annotation)
  return web.json_response({
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
  })

app = web.Application()
app.add_routes([web.post('/', handle)])
app.add_routes([web.post('/light', light_handle)])

if __name__ == '__main__':
  web.run_app(app)