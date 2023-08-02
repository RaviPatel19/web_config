from odoo import fields, models, api


class ResConfigSetting(models.TransientModel):
    _inherit = "res.config.settings"

    dr_route = fields.Many2one(related='website_id.dr_route', domain=[('sale_selectable', '=', True)], readonly=False)
