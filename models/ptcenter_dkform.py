from odoo import models, fields, api
from datetime import datetime, timedelta
import pandas as pd
from pandas import DataFrame
import openpyxl
import xlrd
from io import BytesIO

class PtcenterDkform(models.Model):
    _name = 'ptcenter.dkform'
    _description = '打卡数据表'
    name = fields.Many2one('ptcenter.user', string='法名')
    my_class = fields.Many2one(related='name.class_id',readonly=True,string='班级', store=True)
    date = fields.Date(string='考核日期',default=fields.Date.today)
    week = fields.Char(string='考核周', compute="_compute_week_and_month", inverse='_set_date', store=True,readonly=True)
    month = fields.Char(string='考核月', compute="_compute_week_and_month", inverse='_set_date', store=True,readonly=True)
    dingke = fields.Integer(string='定课遍数')
    wensi = fields.Integer(string='闻思时间')
    cijing = fields.Integer(string='慈经遍数')
    langsong = fields.Integer(string='原文诵读')
    daka = fields.Integer(string='菩提打卡')
    yiri = fields.Char(string='一日一转')
    zixiu = fields.Integer(string='自修遍数')
    yindao = fields.Integer(string='引导吃素')
    tougao = fields.Integer(string='网站投稿')
    fuwu = fields.Float(string='服务时长')
    dushu = fields.Integer(string='读书会次数')
    cishan = fields.Char(string='服务大众')
    chuandeng = fields.Integer(string='传灯次数')
    banxiu = fields.Char(string='是否班修')
    zuxiu = fields.Char(string='是否组修')
    tigang = fields.Char(string='本周列提纲')
    # 2022-06-11  update
    write_time = fields.Integer(string='填写时长')
    write_device = fields.Char('填写设备')
    write_ip = fields.Char('填写IP')

    def report_data(self):
        # 导出表格

        for i in self:
            print(i.name,i.date,i.dingke)
        print('功能更新中',self)

    def write_xlsx(self):
        # 将数据写入xlsx
        # 获取模版文件，复制一份。并重命名
        data = pd.read_excel('')


    # 自动计算周
    @api.depends('date')
    def _compute_week_and_month(self):
        for ch in self:
            today = datetime.strptime(str(self.date), '%Y-%m-%d')
            monday = datetime.strftime(today - timedelta(today.weekday()), "%m.%d") # 05.20
            sunday = datetime.strftime(today + timedelta(7 - today.weekday() - 1), "%m.%d")
            new_monday = str(int(monday.split('.')[0])) + '.' + monday.split('.')[1]
            new_sunday = str(int(sunday.split('.')[0])) + '.' + sunday.split('.')[1]
            ch.week = new_monday + '-' + new_sunday
            month_dict = {"一月份": "1", "二月份": "2", "三月份": "3", "四月份": "4",
                          "五月份": "5", "六月份": "6", "七月份": "7", "八月份": "8",
                          "九月份": "9", "十月份": "10", "十一月份": "11", "十二月份": "12", }
            m = new_monday.split('.')[0] if  int(new_sunday.split('.')[1]) < 4 else  new_sunday.split('.')[0]
            for key, val in month_dict.items():
                if val == m: ch.month = key

    @api.depends('date')
    def _set_date(self):
        for record in self:
            today = datetime.strptime(str(self.date), '%Y-%m-%d')
            monday = datetime.strftime(today - timedelta(today.weekday()), "%m.%d")  # 05.30
            sunday = datetime.strftime(today + timedelta(7 - today.weekday() - 1), "%m.%d")  # 6.05
            new_monday = str(int(monday.split('.')[0])) + '.' + monday.split('.')[1]
            new_sunday = str(int(sunday.split('.')[0])) + '.' + sunday.split('.')[1]
            # 周
            record.week = new_monday + '-' + new_sunday
            month_dict = {"一月份":"1","二月份":"2","三月份":"3","四月份":"4",
                          "五月份":"5","六月份":"6","七月份":"7","八月份":"8",
                          "九月份":"9","十月份":"10","十一月份":"11","十二月份":"12",}
            m = new_monday.split('.')[0] if  int(new_sunday.split('.')[1]) < 4 else  new_sunday.split('.')[0]
            for key ,val in month_dict.items():
                if val == m: record.month = key


