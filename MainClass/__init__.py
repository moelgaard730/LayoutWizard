# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MainClass
                                 A QGIS plugin
 Første udkast
                             -------------------
        begin                : 2015-06-30
        copyright            : (C) 2015 by kmr
        email                : kmr@randers.dk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MainClass class from file MainClass.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .MainModule import MainClass
    return MainClass(iface)
