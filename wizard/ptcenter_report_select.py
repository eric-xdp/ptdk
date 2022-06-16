from odoo import fields, models, _, api
import logging, shutil, openpyxl, os

_logger = logging.getLogger(__name__)

class ReportSelect(models.TransientModel):
    _name = 'ptcenter.report.select'
    _description = '瞬态模型，用来导出数据时，做数据筛选条件；数据并不会保存到数据库。'

    myclass = fields.Many2one('ptcenter.class', string="班级" , required=True)
    month = fields.Selection([('一月份','一月份'),('二月份','二月份'),('三月份','三月份'),('四月份','四月份'),
                              ('五月份','五月份'),('六月份','六月份'),('七月份','七月份'),('八月份','八月份'),
                              ('九月份','九月份'),('十月份','十月份'),('十一月份','十一月份'),('十二月份','十二月份')],
                             string="考核月",default="")

    def get_data_and_write_xlsx(self):
        _logger.info("筛选条件{}, {}".format(self.month,self.myclass.name))
        url = '/dk_report?my_class={}&month={}'.format(self.myclass.name,self.month)
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
            'tfs_close': True
        }

    @api.onchange('month')
    def month_onchange(self):
        if self.month:
            dk = self.env['ptcenter.dkform'].sudo().search([('my_class','=', self.myclass.name),('month','=',self.month)])
            print(dk)
            msg = {'warning': {'title': "提示",'message': "该班本月有{} 条数据可导出。".format(len(dk))} }\
                if dk else {'warning': {'title': "提示",'message': "该班本月暂无数据可导出！"} }
            return msg
        else:
            return

    # 复制模板文件，并重新命名，并返回新文件
    def copy_xlsx(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        source_file = '{}/班级学员月度达标率_模版.xlsx'.format(current_path)
        my_xlsx = '{}/{}学员月度达标率_{}.xlsx'.format(current_path,self.myclass.name, self.month)
        return shutil.copyfile(source_file, my_xlsx)