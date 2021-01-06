#! /usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/joe/python-app/')
from python-kafka import app as application
application.secret_key = 'anything you wish'
