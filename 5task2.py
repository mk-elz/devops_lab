#!/usr/bin/env python

import platform
import sys
import os
import pip
import site
from pip._internal.operations.freeze import freeze
import yaml
import json

instPkgL = []
for requirement in freeze(local_only=True):
    instPkgL.append(requirement)
pyInfo = {'PythonVer': platform.python_version(),
          'VirtualEnvironmentName': sys.prefix.split('/')[-1],
          'PythonExecutableLocation': sys.executable,
          'PythonEnVarPath': os.environ['PYTHONPATH'].split(os.pathsep),
          'PipPath': pip.__path__[0],
          'SitePkgsPath': site.getsitepackages(),
          'InstalledPkgList': instPkgL
          }

print(pyInfo)

with open('pyInfo.yaml', 'w') as outfileYaml:
    yaml.dump(pyInfo, outfileYaml, default_flow_style=False)
with open('pyInfo.json', 'w') as outfileJson:
    json.dump(pyInfo, outfileJson, sort_keys=False, indent=5, ensure_ascii=False)
