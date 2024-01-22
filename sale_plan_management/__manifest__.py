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
    'name': 'Sale Plan Management',
    'version': '16.0.1.0.2',
    'summary': 'Sale Plan Customization',
    'description': 'Sale Plan Customization',
    'author': 'SHL MDG',
    'company': 'Myanmar Distribution Group Co.,Ltd',
    'maintainer': 'SHL MDG',
    'category': 'Sale',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/view_tablet_information.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
