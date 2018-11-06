
from mq import *
import sys, time

mq = MQ()

def LPGLevel():
    perc = mq.MQPercentage()
    return perc["GAS_LPG"]

def COLevel():
    perc = mq.MQPercentage()
    return perc["CO"]

def SmokeLevel():
    perc = mq.MQPercentage()
    return perc["SMOKE"]
