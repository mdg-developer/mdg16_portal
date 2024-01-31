# -*- coding: utf-8 -*-

import logging
from odoo import models, fields
from odoo import fields, models, api, _
from odoo.osv import expression
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF, safe_eval
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class QueueJob(models.Model):
    _inherit = 'queue.job'

    @api.model
    def clear_message(self):
        result = _('')
        for job in self:
            self._cr.execute("update queue_job set result = %s where id = %s",(result,job.id,))
        return True

    @api.model
    def _get_subscribe_users_domain(self):
        domain = super(QueueJob, self)._get_subscribe_users_domain()
        domain.append(('is_subscribe_job', '=', True))
        return domain

    def action_wizard_open_for_multi(self):
        return {
            'name': "Queue Job Multi",
            'type': 'ir.actions.act_window',
            'res_model': 'connector.wizard',
            'view_mode': 'form',
            'active_ids': self.ids,
            'target': 'new',
            'view_id': self.env.ref('connector_ext.view_clear_message_wizard_form').id,
        }
