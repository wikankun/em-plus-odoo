from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")

    responsible_id = fields.Many2one('res.users',
            ondelete='set null', string="Responsible", index=True)
