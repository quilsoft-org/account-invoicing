# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
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
##############################################################################
{
    'name': 'Sale Order Type Dummy Confirmation Integration',
    'version': '8.0.1.0.0',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'depends': [
        'sale_dummy_confirmation',
        'sale_order_type',
        ],
    'category': 'Sale Management',
    'description': '''
Sale Order Type Dummy Confirmation Integration
==============================================
We add dummy confirm option on sale types. If company has "dummy confirm"
then all orders will be "dummy confirm", if not, then we will chec if
sale type has "dummy confirm" or not.
    ''',
    'demo': [
    ],
    'data': [
        'sale_order_type_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}