from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    branch_id = fields.Many2one('res.branch',string="Branch")