# coding=utf-8
import os

import yaml

fp = open(os.path.join(os.getcwd(), 'configs.yml'))
model_configs = yaml.load(fp.read(), Loader=yaml.FullLoader)

print(model_configs)
