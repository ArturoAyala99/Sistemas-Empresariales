from contextlib import nullcontext
from itertools import product
from django.shortcuts import render
from django.http import HttpResponse, response
# import requests
import xmlrpc.client
import json
import base64
import sys
import json 
import os
from dotenv import load_dotenv #borrar el dotoenv en las descargas de pip

load_dotenv()  # take environment variables from .env.

class connectionOddo(): ##el constructor se debe llamar igual que la clase

    models = None
    common = None
    output = None
    uid = None
    url =  ""
    db = ""
    password = ""
    user = ""

    def __init__(self, *args):

        self.url = "http://192.168.0.10:8069"
        self.db = "abarrotes"
        self.password =  "aa11223344"
        self.user =  "arturoayax3@gmail.com" #arturoayax3@gmail.com

        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.output = self.common.version()
        self.uid = self.common.authenticate(self.db,self.user, self.password, self.output)
        #self.models.execute_kw(self.db, self.uid, self.password,'res.partner', 'search',[[['is_company', '=', True]]])



