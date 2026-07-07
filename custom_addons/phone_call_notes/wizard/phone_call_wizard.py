# -*- coding: utf-8 -*-
from odoo import models, fields

class PhoneCallWizard(models.TransientModel):
    _name = 'phone.call.wizard'
    _description = 'Phone Call Wizard'

    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    phone = fields.Char(string='Phone Number', readonly=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('connected', 'Connected'),
        ('busy', 'Busy'),
        ('no_answer', 'No Answer')
    ], string='Status', required=True, default='pending')
    notes = fields.Text(string='Notes')

    def action_save(self):
        self.ensure_one()
        self.env['phone.call.log'].create({
            'partner_id': self.partner_id.id,
            'status': self.status,
            'notes': self.notes,
        })
        return {'type': 'ir.actions.act_window_close'}
