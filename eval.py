from flask import Flask, request
from flask import make_response
from flask_restful import Resource, Api
from flask_cors import CORS

import json
import time
import os
import json
import os
import random
import natsort
import argparse

from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import OrderedDict
import numpy as np

import torch


seed = 1111

app = Flask(__name__)
cors = CORS(app, resources={
  r"/evaluation": {"origin": "*"},
})
api = Api(app)

class JENTIOCR(Resource):
    def __init__(self):
        pass
    def post(self):
        return 12313223123123123

            
api.add_resource(JENTIOCR, '/evaluation')

if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0', port=80)

