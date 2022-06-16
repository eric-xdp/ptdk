from odoo import models, fields

class PtcenterClass(models.Model):
    _name = 'ptcenter.class'
    _description = '班级表'
    name = fields.Char(string='班级名称')
    _sql_constraints = [('unique_class_name', 'unique(name)', '班级名称不能重复')]
    mygroup_id = fields.Many2one('ptcenter.mygroup', string='所属班小组')
    standard_id = fields.Many2one('ptcenter.class.standard', string='班级标准')
    user_id = fields.One2many('ptcenter.user', 'class_id',string='班级学员')
    run_date = fields.Date(string='启动日期',default=fields.Date.today)