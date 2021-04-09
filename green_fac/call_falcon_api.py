# coding=utf-8
import os
import json
import base64

tmp_json_file = "result.json"
curl_cmd = "curl -X POST 'http://10.177.40.228:8000/face/v1/retouch'"
curl_cmd = curl_cmd + " -H 'Content-Type: application/json'"
curl_cmd = curl_cmd + " -H 'X-Auth-Token: <token>'"
curl_cmd = curl_cmd + " -d " + '\'{"image_url":"http://www.hi-chic.com/uploads/allimg/201129/1_201129150227_1_lit.png"}\''
curl_cmd = curl_cmd + " > " + tmp_json_file
os.system(curl_cmd)

with open("result.json", "r") as load_f:
    load_dict = json.load(load_f)
    img_b64_data = load_dict['data']['image_base64']
    with open("result.jpeg", "wb") as fw:
        img_data = base64.b64decode(img_b64_data)
        fw.write(img_data)

os.remove(tmp_json_file)
