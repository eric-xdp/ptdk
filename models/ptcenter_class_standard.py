from odoo import models, fields

class PtcenterClassStandard(models.Model):
    _name = 'ptcenter.class.standard'
    _description = '班级考核标准'
    name = fields.Integer(string='考核标准')
    valid_month = fields.Integer(string='有效月份')
    remark = fields.Char(string='考核说明')
    class_own = fields.Many2one('ptcenter.class', string='所属班级')
    standard_1 = fields.Char(string='标准1')
    standard_2 = fields.Char(string='标准2')
    standard_3 = fields.Char(string='标准3')
    standard_4 = fields.Char(string='标准4')
    standard_5 = fields.Char(string='标准5')
    standard_6 = fields.Char(string='标准6')
    standard_7 = fields.Char(string='标准7')
    standard_8 = fields.Char(string='标准8')