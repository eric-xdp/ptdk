from odoo import models, fields

class PtcenterAttendance(models.Model):

    _name = 'ptcenter.attendance'
    _description = '考勤人数表'
    user_num = fields.Integer(string='考勤人数')
    valid_month = fields.Integer(string='有效月份')
    class_own = fields.Many2one('ptcenter.class', string='所属班级')
    remark = fields.Char(string='备注')
