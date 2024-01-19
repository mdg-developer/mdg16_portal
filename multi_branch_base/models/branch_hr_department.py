from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class HrDepartment(models.Model):
    
    _inherit = 'hr.department'

    branch_id = fields.Many2one('res.branch',string="Branch")
 
    @api.onchange('branch_id')
    def onChangeBranchID(self):
        domain = {}
        if self.branch_id:
            # domain['parent_id'] = [('branch_id', 'in', (self.branch_id.ids))]
            domain['parent_id'] = [('id', 'in', (1,2))]
        else:
            domain['parent_id'] = []
        return {'domain': domain}