#######################################################################
##
## installGMSH.py
##
## Copyright (C) 2016 Idesbald Van den Bosch
##
## This file is part of Puma-EM.
## 
## Puma-EM is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Puma-EM is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Puma-EM.  If not, see <http://www.gnu.org/licenses/>.
##
## Suggestions/bugs : <vandenbosch.idesbald@gmail.com>
##
#######################################################################

import os

def installGMSH():
    URL = "http://www.geuz.org/gmsh/bin/Linux/"
    TARGET = "gmsh-2.6.1-Linux"
    os.system("wget " + URL + TARGET + ".tgz")
    os.system("tar xzf " + TARGET + ".tgz")
    os.system("mv " + os.path.join(TARGET, "bin/gmsh") + " /usr/bin")    
    os.system("rm -rf " + TARGET + ".tgz")

if __name__=="__main__":
    installGMSH()


