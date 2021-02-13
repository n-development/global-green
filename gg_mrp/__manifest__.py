################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2019 N-Development (<https://n-development.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################


{
    'name': "GlobalGreen MRP Customization",
    'summary': """
        The main purpose of the module is to customize for user. 
    """,
    'description': """
    """,
    'version': '14.0.0.0.1',
    'author': "N-Development",
    'category': 'Extra Tools',
    'website': 'https://www.n-development.com',
    'depends': [
        'base', 'mrp'
    ],
    "data": [
        'views/mrp_production.xml'
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
