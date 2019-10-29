from celery_task import app

import datetime
import logging
from time import sleep


@app.task
def say_hello():
    for i in range(10):
        print("start sleep for the {} time".format(i))
        sleep(1)
        logging.info("hello at {}".format(datetime.datetime.now()))
    return "Well done!"


@app.task
def beat():
    print("beat at the {} time".format(datetime.datetime.now()))
    logging.info("HAHAHA beat hello at {} modified".format(datetime.datetime.now()))

