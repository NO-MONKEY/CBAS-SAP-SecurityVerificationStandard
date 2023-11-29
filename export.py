#!/usr/bin/env python

''' Tool for converting the OWASP CBAS SAP Security Maturity Model controls to various formats.

    Usage: ./export.py [--format <csv/xml/json]

    Copyright (c) 2020 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import argparse
import yaml
from cbas import CBASSMM

parser = argparse.ArgumentParser(description='Export the CBAS SAP SMM requirements.')
parser.add_argument('--format', choices=['json', 'xml', 'csv'], default='json')
parser.add_argument('--language', default='en')
parser.add_argument('--config', default='export.yaml')

args = parser.parse_args()

with open(args.config, mode='r') as configfile:
    config = yaml.safe_load(configfile)

    m = CBASSMM(source_language=args.language, config=config)

    if args.format == "csv":
        print(m.to_csv())
    elif args.format == "xml":
        print(m.to_xml())
    else:
        print(m.to_json())
