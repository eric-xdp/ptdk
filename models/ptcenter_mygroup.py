from odoo import models, fields

class PtcenterMygroup(models.Model):
    _name = 'ptcenter.mygroup'
    _description = '班小组'
    name = fields.Char(string='班小组名称')
    city = fields.Char(string='城市')