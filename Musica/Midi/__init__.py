####################################################################################################
#
# Musica - A Music Theory Package for Python
# Copyright (C) 2017 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

####################################################################################################

import gettext
import os

####################################################################################################

# https://docs.python.org/3/library/gettext.html
# http://babel.pocoo.org/en/latest/index.html
# https://www.mattlayman.com/2015/i18n.html

_locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
gettext.install('Musica', _locale_path)