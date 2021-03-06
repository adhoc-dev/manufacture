# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api


class MrpProductProduce(models.TransientModel):

    _inherit = 'mrp.product.produce'

    @api.multi
    @api.constrains('consume_lines')
    def validate_quantity(self):
        for rec in self:
            for line in rec.consume_lines:
                location_id = self._context.get('location_src', False)
                if location_id and line.lot_id:
                    line.lot_id.validate_lot_quantity(
                        line.product_qty, [
                            ('location_id', '=', location_id),
                            ('reservation_id', '=', False)])
