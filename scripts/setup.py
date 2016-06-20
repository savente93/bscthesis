# Copyright 2016 Daniel Vente
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of version 3 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
setup.py file for squint SWIG
"""

from distutils.core import setup, Extension


squint_module = Extension("_squint",
                           sources=["squint_wrap.cxx", "squint.cpp"])

setup(	name = "squint",
		version = "1.0",
		author      = "Daniel Vente",
		author_email = "danvente@gmail.com",
		description = """A python wrapper for the squint code.""",
		ext_modules = [squint_module],
		py_modules = ["squint"])