# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import logging
from odoo import models, fields


_logger = logging.getLogger(__name__)


class Branch(models.Model):
    """res branch"""
    _name = "res.branch"
    _description = 'Company Branches'
    _check_company_auto = True
    _order = 'name'

    name = fields.Char(string='Branch', required=True, store=True, check_company=True)
    branch_code = fields.Char(string='Branch Code', required=True, store=True)
    geo_lat = fields.Char(string='Geo Latitude')
    geo_long = fields.Char(string='Geo Longitude')
    company_id = fields.Many2one('res.company', required=True, string='Company')
    street = fields.Char(string="Street", check_company=True)
    street2 = fields.Char(string="Street 2", check_company=True)
    zip = fields.Char(string="Zip", check_company=True)
    city = fields.Char(string="City", check_company=True)
    state_id = fields.Many2one(
        'res.country.state',
        string="Fed. State", domain="[('country_id', '=?', country_id)]", check_company=True
    )
    country_id = fields.Many2one('res.country',  string="Country")
    email = fields.Char(store=True, check_company=True)
    phone = fields.Char(store=True, check_company=True)
    website = fields.Char(readonly=False, check_company=True)
    branch_manager_id = fields.Many2one('hr.employee', string="Branch Manager", check_company=True)
    second_branch_manager_id = fields.Many2one('hr.employee', string="Second Branch Manager", check_company=True)
    parent_branch_id = fields.Many2one('res.branch', string="Parent Branch", check_company=True)
    radius = fields.Char(string='Radius(meters)')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The Branch name must be unique !'),
        ('branch_code_uniq', 'unique (branch_code)', 'The Branch code must be unique !')
    ]
