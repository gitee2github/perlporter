#!/usr/bin/python3
"""
setup file for perlporter
"""
# ******************************************************************************
# Copyright (c) Huawei Technologies Co., Ltd. 2020-2020. All rights reserved.
# licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.
# Author: Chendong
# Create: 2020-07-31
# Description: provide a tool to package perl module automatically
# ******************************************************************************/

import setuptools

NAME = "perlporter"
VERSION = "0.1"
DESCRIPTION = "A rpm packager bot for perl modules from cpan.org"
LONG_DESCRIPTION = """\
A rpm packager bot for perl modules from cpan.org.

Now it is under developing, any suggestions is appreciated.
"""
AUTHOR = "Chendong1995"
AUTHOR_EMAIL = 'sunchend@outlook.com'
LICENSE = "Mulan PSL v2"
PLATFORMS = "Any"
URL = "https://gitee.com/openeuelr/perlporter"
CLASSIFIERS = [
    'Environment :: Console',
    'License :: Mulan PSL v2',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]

if __name__ == '__main__':
    setuptools.setup(
        name=NAME,
        version=VERSION,
        url=URL,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        classifiers=CLASSIFIERS,
        long_description=LONG_DESCRIPTION,
        scripts=['perlporter']
    )
