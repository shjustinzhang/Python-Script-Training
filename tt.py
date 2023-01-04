
import os
import csv
import sys,re
import shutil
import binascii
import fileinput
import pandas as pd
from csv import reader
from xml.dom import minidom
from pandas import DataFrame
from pandas import ExcelWriter
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
from pandas import DataFrame, ExcelWriter
from var_dump import var_dump
import json
import time
from papi2.register_accessor import RegisterAccessor
from progress.bar import IncrementalBar
import winsound
import configparser

sys.path.append("C:\AMD\Kysy4\Python")

import KysyEnvironment
import Kysy

import requests
from bs4 import BeautifulSoup

Z ='{0:0{1}x}'.format(15, 4)
print(Z)
Z ='{0:0{1}X}'.format(15, 4)
print(Z)
Z ='{0:0{1}X}'.format(21, 4)
print(Z)
Z ='{0:0{1}b}'.format(15, 4)
print(Z)
Z ='{0:#{1}X}'.format(15, 4)
print(Z)
Z = str(bin(15)).zfill(3)
print(Z)
Z = str(bin(15)).zfill(7)
print(Z)

print(int('100',2)) # 2表示这里的100 其实是二进制，那100 作为2进制就是 4
print(len('e000745c45543fbce8ac0aab8001d15715570001a2e22aa1fde34560555c00068ab8aa800006'))
print(bin(0x34560000021038098ab000001))
print(hex(0b000000010000100000011100000001001100010101011000000000000000000000001))



