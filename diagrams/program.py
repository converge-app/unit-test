#!/bin/python

import os
import pathlib
from termcolor import colored

findAllSvgs = os.popen('find . | grep "svg"').readlines()

paths = []
for filePath in findAllSvgs:
    path = pathlib.Path(filePath[:-1])
    if path.exists:
        paths.append({
            'name': path.name,
            'name-without-ext': os.path.splitext(path.name)[0],
            'full-path': path,
            'path': path.parent,
            'full-path-without-ext': os.path.splitext(path)[0]
        })
    else:
        raise Exception("Couldn't process: " + path.as_posix())
for path in paths:
    print('Processing:', path['name'])
    pathSvg = path['full-path']
    pathPdf = path['full-path-without-ext'] + ".pdf"
    print('  source: ', pathSvg)
    print('  dest:   ', pathPdf)
    os.system(f'inkscape -C -z --file={pathSvg} --export-pdf={pathPdf}')
    if os.path.exists(pathPdf):
        print(colored('  ok!', 'green'))
    else:
        print(colored('  failed!', 'red'))
        raise Exception("Couldn't process: " + pathSvg.as_posix())

print(colored("All ok", 'green'))
