import logging
import os
from flask import Flask
import time
from Config import getServerConfig

app = Flask(__name__)
app.config['DEBUG']=True

# API stuffs to create flask API



# Setting up a personal logging method
def initLoggingConfig (filepath):
    format= "%(asctime)s : %(message)s"
    logging.basicConfig(filename=filepath, format=format, level=logging.INFO, datefmt="%d/%m/%Y %I:%M:%S %p")



# Execution of code starts from here
serverConfig= getServerConfig()

logFileDir= serverConfig['logFileDir']
if os.path.exists(logFileDir) == False:
    print("Logfile Directory "+ logFileDir+ " is not exist. Exiting the app")
    exit(-1)

print("Logfile directory "+logFileDir)
initLoggingConfig(logFileDir + "/app.log")

logging.info('ServerConfig => %s', serverConfig)


port = serverConfig['port']

app.run('localhost', port)

