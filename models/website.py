import os
from odoo import api, fields, models, _

class Website(models.Model):
    _inherit = "website"

    is_production = fields.Boolean(compute='_compute_is_production', string='Is Production')
    
    def _compute_is_production(self):
        prod = os.environ.get("ODOO_STAGE") == "production"
        for website in self:
            website.is_production = prod