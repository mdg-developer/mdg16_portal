from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
import logging

_logger = logging.getLogger(__name__)

class ConnectorWizard(models.TransientModel):

    _name = 'connector.wizard'
    _description = 'Wizard for Clear Messages, Reque Jobs, Set To Done'

    queue_job_id = fields.Many2one('queue.job', string='Queue Job')

    def clear_messages(self):
        job_ids = self.env.context.get('active_ids', [])
        if job_ids:
            job_ids = self.env['queue.job'].search([('id','in',job_ids)])
            for job_id in job_ids:
                # job_id.write({'state':'approved'})
                self.env.cr.execute("update queue_job set result =%s where id =%s", ('', job_id.id,))
