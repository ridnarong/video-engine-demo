Video Engine Demo
==================
Python example code 

Runtime
---------
### HTTP Request
#### Request
**Method**
POST

**Headers**
- Content-Type: multipart/form-data
- AGENT-ID: *AGENT_ID*

**Request Body**
- images[i]: *File {image binary}*
- data: *File {JSON data}*

#### Response
**Status**
200

**Headers**
- Content-Type: application/json

**Response Body**
```
{
    "Field": {
      <string>: <number>
    },
    "Property": {
      <string>: <string>
    },
    "Result": <JSON string>
}
```
### Linux process
**exec**
*executable file*

**args**
*array of arguments*

**Environment variable**
- AGENT_ID: *AGENT_ID*
- DATA: *JSON String*
- IMAGE_PATH: *comma separated image full path*
- STREAM_URL: *accessible stream URL*

**Standard output**
*One line per record: JSON String*

Example
---------
### HTTP Request
#### Request
**Method**
POST

**Headers**
- Content-Type: multipart/form-data
- AGENT-ID: 111

**Request Body**
- images[0]:
```
filename: /nectec-camera-snapshot.s3.meca.in.th/NECTEC-CAM-6/6B0201EPAG7F42D/2022-09-28/001/jpg/09/52/15[R][0@0][0].jpg
body: image binary
```
- data:
```
filename: data.json
body: {
  "media": "images",
  "cameraID": "cameras:NECTEC:6B0201EPAG7F42D",
  "dateQuery": {
      "range": {
          "start": "now-2m",
          "end": "now"
      },
      "limit": {
          "last": 1
      }
  },
  "properties": "{\"threshold\":123}",
  "annotations": "{\"source-ref\":\"/foo-202209121239.jpeg\",\"annotations\":{\"light-source\":[{\"id\":\"#f4683761-ed9d-4fed-bad6-a9e0ae5c175c\",\"shape\":\"rect\",\"x\":276,\"y\":188,\"w\":78,\"h\":97},{\"id\":\"#44068ba9-b9eb-48da-a488-ab5f2e1585a7\",\"shape\":\"rect\",\"x\":1113,\"y\":83,\"w\":32,\"h\":58}]}}",
  "mediaURL": [
      "https://nectec-camera-snapshot.s3.meca.in.th/NECTEC-CAM-6/6B0201EPAG7F42D/2022-09-28/001/jpg/09/52/15%5BR%5D%5B0%400%5D%5B0%5D.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=MRPF3M4518D2TFLRDR7X%2F20220928%2FREGION%2Fs3%2Faws4_request&X-Amz-Date=20220928T025220Z&X-Amz-Expires=900&X-Amz-Signature=1351e92f86c7d85626d135dafcde77cce5b2533c21f7e9e5c82fbdda10be0a9f&X-Amz-SignedHeaders=host&x-id=GetObject"
  ]
}
```

#### Response
**Status**
200

**Headers**
- Content-Type: application/json

**Response Body**
```json
{
 "Field": { "Off": 2, "All": 2 },
 "Property": { "CameraID": "6B0201EPAG7F42D" },
 "Result": "{\"regions\": [{\"id\": \"#f4683761-ed9d-4fed-bad6-a9e0ae5c175c\", \"shape\": \"rect\", \"x\": 276, \"y\": 188, \"w\": 78, \"h\": 97, \"result\": \"off\"}, {\"id\": \"#44068ba9-b9eb-48da-a488-ab5f2e1585a7\", \"shape\": \"rect\", \"x\": 1113, \"y\": 83, \"w\": 32, \"h\": 58, \"result\": \"off\"}]}"
}
```
### Linux process
**exec**
`/home/ridnarong/workspaces/video-engine-demo/.venv/bin/python`

**args**
`["/home/ridnarong/workspaces/detect-people/light.py"]`

**Environment variable**
- AGENT_ID: 111
- DATA: 
```json
{
  "media": "images",
  "cameraID": "cameras:NECTEC:6B0201EPAG7F42D",
  "dateQuery": {
      "range": {
          "start": "now-2m",
          "end": "now"
      },
      "limit": {
          "last": 1
      }
  },
  "properties": "{\"threshold\":123}",
  "annotations": "{\"source-ref\":\"/foo-202209121239.jpeg\",\"annotations\":{\"light-source\":[{\"id\":\"#f4683761-ed9d-4fed-bad6-a9e0ae5c175c\",\"shape\":\"rect\",\"x\":276,\"y\":188,\"w\":78,\"h\":97},{\"id\":\"#44068ba9-b9eb-48da-a488-ab5f2e1585a7\",\"shape\":\"rect\",\"x\":1113,\"y\":83,\"w\":32,\"h\":58}]}}",
  "mediaURL": [
      "https://nectec-camera-snapshot.s3.meca.in.th/NECTEC-CAM-6/6B0201EPAG7F42D/2022-09-28/001/jpg/09/52/15%5BR%5D%5B0%400%5D%5B0%5D.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=MRPF3M4518D2TFLRDR7X%2F20220928%2FREGION%2Fs3%2Faws4_request&X-Amz-Date=20220928T025220Z&X-Amz-Expires=900&X-Amz-Signature=1351e92f86c7d85626d135dafcde77cce5b2533c21f7e9e5c82fbdda10be0a9f&X-Amz-SignedHeaders=host&x-id=GetObject"
  ]
}
```
- IMAGE_PATH: `/tmp/people-counting-process-demo/1663602956772.172.16.2.50_01_20220919225021474_TIMING.jpg`

**Standard output**
`{"Field": { "Off": 2, "All": 2 }, "Property": { "CameraID": "6B0201EPAG7F42D" }, "Result": "{\"regions\": [{\"id\": \"#f4683761-ed9d-4fed-bad6-a9e0ae5c175c\", \"shape\": \"rect\", \"x\": 276, \"y\": 188, \"w\": 78, \"h\": 97, \"result\": \"off\"}, {\"id\": \"#44068ba9-b9eb-48da-a488-ab5f2e1585a7\", \"shape\": \"rect\", \"x\": 1113, \"y\": 83, \"w\": 32, \"h\": 58, \"result\": \"off\"}]}"}`

Demo
---------
Create virtual environment
```bash
$ python3 -m venv .venv
```

Enter virtual environment
```bash
$ . .venv/bin/activate
```

Install dependency
```bash
$ pip install -r requirements.txt
```
Start HTTP Service
```bash
$ python server.py
```

Process Image using HTTP Request
```bash
$ curl -F images[0]=@foo-202209121239.jpeg -F data=@data.json -H AGENT_ID=111 localhost:8080/light
```

Process Image using Python
```bash
$ export AGENT_ID=111; export DATA=$(cat data.json); export IMAGE_PATH="${PWD}/foo-202209121239.jpeg"; python light.py
```

Process Stream using Python
```bash
$ export DATA=$(cat data.json); export STREAM_URL="rtsp://user:password@1.2.3.4:554/Streaming/Channels/101/"; python light.py
```
