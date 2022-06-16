import datetime
from odoo import http
from odoo.http import request, content_disposition
from collections import Counter
import logging, shutil, openpyxl, os
from io import BytesIO

_logger = logging.getLogger(__name__)

class Dkform(http.Controller):
    # 获取所有的班级,以及对应的学员
    @http.route('/api/get_class', type='http', auth='public', csrf=False, cors='*')
    def get_class(self):
        """
        return: {'测试一班': ['小明', '小红'], '测试二班': ['小白', '小绿']}
        """
        class_info = request.env['ptcenter.class'].sudo().search([])
        info = {}
        for cls in class_info:
            info[cls.name] = []
            for u in cls.user_id:
                info[cls.name].append(u.name)
        _logger.info("获取班级：%s" % str(info))
        return str(info)

    @http.route('/api/submit_myform', methods=['POST'], type='json',auth='public', csrf=False, cors='*')
    def dk_data(self):
        mydata = request.jsonrequest.get('mydata', None)
        user = request.env['ptcenter.user'].sudo().search([('name', '=', mydata['name']),('class_id','=',mydata['my_class'])])
        # mydata['name'] int 1
        mydata['name'] = user.id
        _logger.info('用户所属班级：%s,用户名: %s' % (user.class_id.name,user.name))
        myDk = request.env['ptcenter.dkform'].sudo().search(
            [('name', '=', mydata['name']), ('date', '=', mydata['date']),('my_class', '=', user.class_id.name)])
        mydata.pop('my_class')
        if not myDk:
            # 没有记录，直接存储
            # 通过名字法名获取user
            result = request.env['ptcenter.dkform'].sudo().create(mydata)
            a = self.week_data(result)
            msg = self.week_msg(a)
            # for dk in result:
            #     # 获取周数据
            #     data = {"status":'新增数据',
            #             "data": {"name":dk.name.name,"my_class":dk.my_class.name,"week":dk.week,"month":dk.month,
            #                      "date":dk.date,"dingke": dk.dingke, "wensi": dk.wensi, "cijing": dk.cijing,
            #                      "langsong": dk.langsong, "daka": dk.daka, "yiri": dk.yiri, "zixiu": dk.zixiu,
            #                      "yindao": dk.yindao,"tougao": dk.tougao, "fuwu": dk.fuwu, "dushu": dk.dushu,
            #                      "cishan": dk.cishan, "chuandeng": dk.chuandeng,"banxiu": dk.banxiu, "zuxiu": dk.zuxiu,
            #                      "tigang": dk.tigang }}
                # self.send_message(data)
            _logger.info("无今日数据，直接新增数据：%s" % msg)
            return msg
        else:
            myDk.write(mydata)
            newdata = request.env['ptcenter.dkform'].sudo().search([('name', '=', mydata['name']), ('date', '=', mydata['date']),('my_class','=',user.class_id.name)])
            # 获取周数据
            a = self.week_data(newdata)
            msg = self.week_msg(a)
            # for dk in newdata:
            #     data = {"status": '修改数据',
            #             "data": {"name":dk.name.name,"my_class":dk.my_class.name,"week":dk.week,"month":dk.month,
            #                      "date":dk.date,"dingke": dk.dingke, "wensi": dk.wensi, "cijing": dk.cijing,
            #                      "langsong": dk.langsong, "daka": dk.daka, "yiri": dk.yiri, "zixiu": dk.zixiu,
            #                      "yindao": dk.yindao,"tougao": dk.tougao, "fuwu": dk.fuwu, "dushu": dk.dushu,
            #                      "cishan": dk.cishan, "chuandeng": dk.chuandeng,"banxiu": dk.banxiu, "zuxiu": dk.zuxiu,
            #                      "tigang": dk.tigang }}
                # self.send_message(data)
            _logger.info("已有今日数据，直接修改数据：%s" % msg)
            return msg
#     def send_message(self, mydata):
#         data = mydata['data']
#         # 定义发送的msg 格式
#         msg_list = [{'法名': data['name']},{'日期': data['date']},{"操作类型":mydata['status']}, {'定课': data['dingke']},
#                     {'闻思': data['wensi']}, {'原文朗诵': data['langsong']},
#                     {'菩提导航': data['daka']}, {'一日一转': data['yiri']}, {'组修': data['zuxiu']}, {'班修': data['banxiu']},
#                     {'慈经': data['cijing']}, {'自修遍数': data['zixiu']}, {'服务大众时长': data['fuwu']},
#                     {'引导吃素': data['yindao']}, {'服务大众': data['cishan']}, {'传灯邀请': data['chuandeng']},
#                     {'列提纲': data['tigang']}, {'举办读书会': data['dushu']}, {'网站投稿': data['tougao']}]
#         # 剔除 否、 0 、 ""
#         removed_list = []
#         for v in msg_list:
#             for key, val in v.items():
#                 for i in ['', False, '否']:
#                     if val == i: removed_list.append(v)
#
#                 if str(val) == 'True': v[key] = '是'
#         for i in removed_list:
#             msg_list.remove(i)
#         msg = """{}  {}
# """.format(msg_list[0]['法名'], msg_list[1]['日期'])
#         for m in msg_list[2:]:
#             for key, val in m.items():
#                 msg+="""{}: {}
# """.format(key, val)
#         wx = SendWeiXinWork()
#         # HaiKuoShaoErYiShuXueYuanHanLaoShi
#         wx.send_message('xudaopu', msg)
#         return msg_list
    @http.route('/api/check_today',methods=['POST'], type='json', auth='public', csrf=False, cors='*')
    def check_today(self):
        name = request.jsonrequest.get('name', None)
        myday = request.jsonrequest.get('mydate',None)
        myclass = request.jsonrequest.get('myclass', None)
        class_info = request.env['ptcenter.class'].sudo().search([('name','=', myclass)])
        run_date = class_info.run_date
        myDk = request.env['ptcenter.dkform'].sudo().search([('name','=',name),('date','=',myday),('my_class','=',class_info.name)])
        # 没有记录，返回后继续填写，有记录的话，获取记录值，返回并将记录值赋值，进行修改
        if not myDk:
            return {'run_date':run_date,'data':True}
        for dk in myDk:
            data = {'run_date':run_date,
                    'data':{
                "dingke": dk.dingke, "wensi": dk.wensi, "cijing": dk.cijing,
                "langsong": dk.langsong, "daka": dk.daka, "yiri": dk.yiri, "zixiu": dk.zixiu, "yindao": dk.yindao,
                "tougao": dk.tougao, "fuwu": dk.fuwu, "dushu": dk.dushu, "cishan": dk.cishan, "chuandeng": dk.chuandeng,
                "banxiu": dk.banxiu, "zuxiu": dk.zuxiu, "tigang": dk.tigang
            }}
            return data

    def week_data(self,data):

        for dk in data:
            user_info = { "name": dk.name.name, "my_class": dk.my_class.name, "week": dk.week,
                          "month": dk.month }
            # dk.week  5.16-5.22
            year = str(dk.date).split('-')[0]
            myweek = dk.week
            # 5.16
            start_date = year + '-' + myweek.split('-')[0].replace('.', '-')
            end_date = year + '-' + myweek.split('-')[1].replace('.', '-')
            t = request.env['ptcenter.dkform'].sudo().search([('name', '=', dk.name.name),
                                                              ('my_class', '=',dk.my_class.name),
                                                              ('date', '>=', start_date),
                                                              ('date', '<=', end_date)])
            yiri_list = []
            banxiu_list = []
            zuxiu_list = []
            tigang_list = []
            cishan = 0
            my_list = []
            for i in range(len(t)):
                if t[i].yiri == "是": yiri_list.append(t[i].yiri)
                banxiu_list.append(t[i].banxiu)
                zuxiu_list.append(t[i].zuxiu)
                tigang_list.append(t[i].tigang)
                if t[i].cishan:
                    if len(t[i].cishan) > 0:
                        cishan += 1
                my_fuwu = int(t[i].fuwu) if t[i].fuwu % 1 == 0 else t[i].fuwu
                my_list.append({"dingke": t[i].dingke, "wensi": t[i].wensi, "cijing": t[i].cijing,
                              "langsong": t[i].langsong, "daka": t[i].daka, "zixiu": t[i].zixiu,
                              "yindao": t[i].yindao, "tougao": t[i].tougao, "fuwu": my_fuwu,
                              "dushu": t[i].dushu, "chuandeng": t[i].chuandeng })
            my_total = Counter({})
            for i in my_list: my_total += (Counter(i))
            total = dict(my_total)
            if len(yiri_list) > 0: total['yiri'] = len(yiri_list)

            if "是" in banxiu_list: total['banxiu'] = "是"
            if "是" in zuxiu_list: total['zuxiu'] = "是"
            if "是" in tigang_list: total['tigang'] = "是"
            if cishan > 0: total['cishan'] = cishan
            my_result = dict(user_info,**total)
            return my_result

    def week_msg(self,data):
        # {"name": dk.name.name, "my_class": dk.my_class.name, "week": dk.week,
         # "month": dk.month}
        msg_list = [{'法名': data['name']},{'考核周': data['week']},
                    {'定课': "dingke"},{'闻思': "wensi"}, {'原文诵读': "langsong"},
                    {'菩提导航': "daka"}, {'一日一转': "yiri"}, {'组修': "zuxiu"}, {'班修': "banxiu"},
                    {'慈经': "cijing"}, {'自修遍数': "zixiu"}, {'服务大众时长': "fuwu"},
                    {'引导吃素': "yindao"}, {'服务大众次数': "cishan"}, {'传灯邀请': "chuandeng"},
                    {'列提纲': "tigang"}, {'举办读书会': "dushu"}, {'网站投稿': "tougao"}]

        unit_dict = {'法名': "",'考核周': "",'定课': "遍",'闻思': "分钟",'原文诵读': "遍",'菩提导航': "次",
                     '一日一转': "次",'组修': "",'班修': "",'慈经': "次",'自修遍数': "遍",'服务大众时长': "小时",
                     '引导吃素': "次",'服务大众次数': "次",'传灯邀请': "次",'列提纲': "",'举办读书会': "次",'网站投稿': "次"}

        # 赋值清洗
        removed_list = []
        for i in msg_list[2:]:
            for k, v in i.items():
                if v not in data.keys():
                    removed_list.append(i)
                else:
                    i[k] = data[v]

        for i in msg_list:
            for k,v in i.items():
                if k in unit_dict.keys():
                    i[k] = str(v) + unit_dict[k]

        for x in removed_list:
            msg_list.remove(x)
        weekday_dict = { 0:'周一',1:'周二',2:'周三',3:'周四',4:'周五',5:'周六',6:'周日'}
        weekday = datetime.datetime.today().weekday()
        msg = """{}  {}
{}
———————
""".format(msg_list[0]['法名'], weekday_dict[weekday], msg_list[1]['考核周'])
        for m in msg_list[2:]:
            for key, val in m.items():
                msg += """{}: {}
""".format(key, val)
        return {"msg":msg}

    @http.route(['/dk_report'], type='http', auth="public", website=True)
    def dk_report(self, **kw):

        my_cls = kw.get('my_class')
        my_month = kw.get('month')
        dk_list_month = []
        dk_data = request.env['ptcenter.dkform'].sudo().search(
            [('my_class', '=', my_cls), ('month', '=', my_month)])
        for i in dk_data:
            dk_list_month.append([i.week, i.month, i.my_class.name, i.name.name,
                                  i.date, i.dingke, i.wensi, i.cijing,
                                  i.langsong, i.daka, i.yiri, i.zixiu,
                                  i.yindao, i.tougao, i.fuwu, i.dushu,
                                  i.cishan, i.chuandeng, i.banxiu, i.zuxiu, i.tigang])
        _logger.info("获取数据，并写入xlsx表中: {}".format(dk_list_month))
        my_file = self.copy_xlsx(my_cls,my_month)
        myxlsx = openpyxl.load_workbook(my_file)
        my_sheet = myxlsx['源数据']
        for r in dk_list_month:
            my_sheet.append(r)
        myxlsx.save(my_file)
        output = BytesIO()
        myxlsx.save(output)
        output.seek(0)
        print(my_file)
        file_name = my_file.split('/')[-1]
        print(file_name)
        response = request.make_response(None,
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition(file_name))
            ]
        )
        response.stream.write(output.read())
        output.close()
        # 删除服务器上导出的文件
        os.remove(my_file)
        return response


    def copy_xlsx(self,cls,month):
        current_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前目录下所有的xlsx文件，存放在列表内
        filelist = []
        for root, dirs, files in os.walk(current_path, topdown=False):
            for name in files:
                str = os.path.join(root, name)
                if str.split('.')[-1] == 'xlsx':
                    if '月份' in str.split('.')[0]:
                        filelist.append(str)
        source_file = '{}/班级学员月度达标率_模版.xlsx'.format(current_path)
        my_xlsx = '{}/{}学员月度达标率_{}.xlsx'.format(current_path,cls, month)
        return shutil.copyfile(source_file, my_xlsx)
import requests
# class SendWeiXinWork():
#     def __init__(self):
#         self.CORP_ID = "ww600ff64abbf30d6a"  # 企业号的标识
#         self.SECRET = "3L8dJCc1oNW60OvEmGF-U5f9t_YFXYqu9wLR8c3V32A"  # 管理组凭证密钥
#         self.AGENT_ID = 1000002  # 应用ID
#         self.token = self.get_token()
#
#     def get_token(self):
#         url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
#         data = {
#             "corpid": self.CORP_ID,
#             "corpsecret": self.SECRET
#         }
#         try:
#             req = requests.get(url=url, params=data)
#             res = req.json()
#             if res['errmsg'] == 'ok':
#                 return res["access_token"]
#             else:
#                 return res
#         except Exception as e :
#             print(e)
#
#
#
#     def send_message(self, to_user, content):
#         url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % self.token
#         data = {
#             "touser": to_user,  # 发送个人就填用户账号
#             # "toparty": to_user,  # 发送组内成员就填部门ID
#             "msgtype": "text",
#             "agentid": self.AGENT_ID,
#             "text": {"content": content},
#             "safe": "0"
#         }
#
#         req = requests.post(url=url, json=data)
#         res = req.json()
#         if res['errmsg'] == 'ok':
#
#             return "send message succeed"
#         else:
#
#             return res


