# -*- coding: utf-8 -*-
###################################################################################
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': 'MDG Sale Order Management',
    'version': '16.0.1.0.2',
    'summary': 'All Mobile Sale Orders, Pre Sale Orders, Direct Sale Orders Customization',
    'description': 'All Mobile Sale Orders, Pre Sale Orders, Direct Sale Orders Customization',
    'author': 'SHL MDG',
    'company': 'Myanmar Distribution Group Co.,Ltd',
    'maintainer': 'SHL MDG',
    'category': 'Sale Orders',
    'depends': ['sale', 'device_management'],
    'data': [
        'views/view_direct_sale_order.xml',
        'views/view_pre_sale_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
