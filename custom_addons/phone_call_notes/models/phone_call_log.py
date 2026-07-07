# -*- coding: utf-8 -*-
from odoo import models, fields

class PhoneCallLog(models.Model):
    _name = 'phone.call.log'
    _description = 'Phone Call Log'
    _order = 'call_date desc'

    partner_id = fields.Many2one('res.partner', string='Customer', required=True, ondelete='cascade')
    phone = fields.Char(string='Phone Number', related='partner_id.phone', readonly=True, store=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('connected', 'Connected'),
        ('busy', 'Busy'),
        ('no_answer', 'No Answer')
    ], string='Status', required=True, default='pending')
    notes = fields.Text(string='Notes')
    call_date = fields.Datetime(string='Date', default=fields.Datetime.now, required=True)
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user, required=True)
