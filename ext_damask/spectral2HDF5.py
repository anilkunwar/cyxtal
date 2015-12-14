#!/usr/bin/env python
# -*- coding: UTF-8 no BOM -*-

"""
   ________  ___  ___________    __
  / ____/\ \/ / |/ /_  __/   |  / /
 / /      \  /|   / / / / /| | / /
/ /___    / //   | / / / ___ |/ /___
\____/   /_//_/|_|/_/ /_/  |_/_____/

Copyright (c) 2015, C. Zhang.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1) Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
2) Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

DESCRIPTION
-----------
python spectral2HDF.py ${RST.spectralOut} [-o outputFileName]
    This script is used to directly convert a spectralOut file from DAMASK
    spectral analysis to a HDF5 file for further data processing.
"""

import os, sys, argparse
import h5py
import numpy as np


###########
# MARCROS #


##########
# PARSER #
parser = argparse.ArgumentParser(prog='sepctral2HDF5',
                                 epilog='require h5py and numpy',
                                 description='convert binary results to hdf5.')
parser.add_argument('sourceFile',
                    help='Binary output file from DAMASK_spectral',
                    default='run.spectralOut')
parser.add_argument('-v', '--version',
                    action='version',
                    version="%(prog)s 0.1")
parser.add_argument('-o', '--output',
                    help='output file name.'
                    default='run.hdf5')
parser.add_argument('-d', '--debug',
                    action='store_true',
                    default=False,
                    help='toggle debug output on terminal.')
parser.add_argument('-s', '--silent',
                    action='store_true',
                    default=False)
args = parser.parse_args()
if not args.silent:
    print "*"*20
    parser.parse_args()
    print "*"


################
# READ IN DATA #
