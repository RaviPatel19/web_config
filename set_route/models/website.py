from odoo import fields, models, api


class Website(models.Model):
    _inherit = 'website'

    dr_route = fields.Many2one('stock.route', domain=[('sale_selectable', '=', True)], string='Default Route')
