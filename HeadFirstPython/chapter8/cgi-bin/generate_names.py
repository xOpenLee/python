#!/usr/bin/python3
# coding=utf-8

import json

import athletemodel
import yate

names = athletemodel.get_names_from_store()

print (yate.start_response('application/json'))
print (json.dumps(sorted(names)))

