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
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

NPDIR = np.get_include()
EXTEN = [ Extension( "ctools",
                    ["ctools.pyx"],
                    include_dirs=[NPDIR, "."]),
          Extension( "cxtallite",
                    ["cxtallite.pyx"],
                    include_dirs=[NPDIR, "."])
        ]

setup(
      name='cyxtal',
      version=0.1,
      description='crystal analysis package (cython)',
      author='C.Z',
      author_email='chenzhang8722@gmail.com',
      packages=["cyxtal"],
      ext_modules=EXTEN,
      cmdclass={'build_ext': build_ext},
)