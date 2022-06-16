from odoo import models, fields

class PtcenterUserType(models.Model):
    _name = 'ptcenter.user.type'
    _description = '用户类型'
    name = fields.Char(string='类型名称')
