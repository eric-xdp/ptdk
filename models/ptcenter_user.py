from odoo import models, fields

class PtcenterUser(models.Model):
    _name = 'ptcenter.user'
    _description = '菩提管理用户表'
    name = fields.Char(string='法名')
    # _sql_constraints = [('unique_user_name', 'unique(name)', '用户法名不能重复')]
    password = fields.Char(stirng='密码')
    sex = fields.Selection([('male', '男'),('female','女')], string='性别')
    age = fields.Integer(string='年龄')
    wechat = fields.Char(string='微信')
    phone = fields.Char(string='手机号')
    join_date = fields.Date(string='进班日期')
    user_status = fields.Selection([('正常','正常'),('不纳入考勤','不纳入考勤'),('暂停','暂停'),('退班','退班')], string='学员状态', default='正常')
    user_type = fields.Many2one('ptcenter.user.type', string='用户类型')
    class_id = fields.Many2one('ptcenter.class', string='所属班级')
    # 排序
    user_seq = fields.Integer(string='学员排序')