from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class HrJob(models.Model):
    
    _inherit = 'hr.job'

    branch_id = fields.Many2one('res.branch',string="Branch")
    parent_position_id = fields.Many2one('hr.job',string="Parent Position")

    @api.onchange('branch_id')
    def onChangeBranchID(self):
        domain = {}
        if self.branch_id:
            domain['department_id'] = [('branch_id', 'in', (self.branch_id.ids))]
        else:
            domain['department_id'] = []
        return {'domain': domain}
    