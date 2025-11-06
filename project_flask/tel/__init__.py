from flask import Blueprint,jsonify
from flask_cors import CORS
from db import query_all,query_one,execute
tel_bp = Blueprint('tel',import_name=__name__,url_prefix='/tel')
CORS(tel_bp)
@tel_bp.route('/test',methods=['GET'])
def test():
    sql = 'select service_type,count(1) as total from cdr_table group by service_type order by service_type'
    results = query_all(sql)
    items = []
    for item in results:
        name = ''
        if item['service_type'] == 1:
            name = '普通话务'
        elif item['service_type'] == 2:
            name = '增值话务'
        else:
            name = '集团规模话务'
        items.append({
            "name": name,
            "value": item['total']
        })
    data = {
        'code':200,
        'msg':'success',
        'data':items,

    }
    return jsonify(data)
@tel_bp.route('/get_procedure_status',methods=['GET'])
def get_procedure_status():
    sql = 'select procedure_status,count(1) as total from cdr_table group by procedure_status order by procedure_status'
    results = query_all(sql)
    items = []
    for item in results:
        name=''
        if item['procedure_status'] == 1:
            name = '2G'
        elif item['procedure_status'] == 2:
            name = '3G'
        elif item['procedure_status'] == 3:
            name = '4G'
        else:
            name = '5G'
        items.append({
            'name':name,
            'value':item['total']
        })
    data = {
        'code':200,
        'msg':'success',
        'data':items
    }
    return jsonify(data)

@tel_bp.route('/get_pie_data',methods=['GET'])
def get_pie_data():
    sql = 'select dx_cause,count(1) as total from cdr_table group by dx_cause order by dx_cause'
    results = query_all(sql)
    pie_data = []
    for item in results:
        name=''
        if item['dx_cause'] == 1:
            name = 'demo1'
        elif item['dx_cause'] == 2:
            name = 'demo2'
        elif item['dx_cause'] == 3:
            name = 'demo3'
        elif item['dx_cause'] == 4:
            name = 'demo4'
        else:
            name = 'demo5'
        pie_data.append({
            'name':name,
            'value':item['total']
        })
    data = {
        'code':200,
        'msg':'success',
        'data':pie_data
    }
    return jsonify(data)

@tel_bp.route('/get_day_count',methods=['GET'])
def get_day_count():
    sql = "select DATE_FORMAT(event_start_date,'%Y-%m-%d') as daytime,count(1) as total from cdr_table group by DATE_FORMAT(event_start_date,'%Y-%m-%d')"
    results = query_all(sql)
    days = []
    counts = []
    for item in results:
        days.append(item['daytime'])
        counts.append(item['total'])
    data = {
        'code':200,
        'msg':'success',
        'data':{
            'days':days,
            'counts':counts
        }
    }
    return jsonify(data)
@tel_bp.route('/get_bar_chart',methods=['GET'])
def get_bar_chart():
    sql = 'select procedure_status,count(1) as total from cdr_table group by procedure_status order by procedure_status'
    results = query_all(sql)
    types = []
    counts = []
    for item in results:
        if item['procedure_status'] == 1:
            type = '2G'
        elif item['procedure_status'] == 2:
            type = '3G'
        elif item['procedure_status'] == 3:
            type = '4G'
        else:
            type = '5G'
        types.append({
            'type':type
        })
        counts.append({
            'count':item['total']
        })
    data = {
        'code':200,
        'msg':'success',
        'data':{
            'types':types,
            'counts':counts
         }
    }
    return jsonify(data)

@tel_bp.route('/get_radar_chart',methods=['GET'])
def get_radar_chart():
    sql = "SELECT COUNT(DISTINCT service_type) as service_types,COUNT(DISTINCT procedure_status) as procedure_statuses,COUNT(DISTINCT dx_cause) as release_reasons,COUNT(DISTINCT source_access_type) as source_access_types,COUNT(DISTINCT dest_access_type) as dest_access_types, COUNT(DISTINCT hide_status) as hide_statuses FROM cdr_table"
    results = query_all(sql)
    service_types = []
    procedure_statuses = []
    release_reasons = []
    source_access_types = []
    dest_access_types = []
    hide_statuses = []
    for item in results:
        service_types.append(item['service_types'])
        procedure_statuses.append(item['procedure_statuses'])
        release_reasons.append(item['release_reasons'])
        source_access_types.append(item['source_access_types'])
        dest_access_types.append(item['dest_access_types'])
        hide_statuses.append(item['hide_statuses'])
    seriesData = [
        {
            'name':'业务数据',
            'value':[service_types,procedure_statuses,release_reasons,source_access_types,dest_access_types,hide_statuses]
        }
    ]
    indicator = [
        {'name':'服务类型分布','max':10},
        {'name': '过程状态分析', 'max': 10},
        {'name': ' 释放原因分析', 'max': 20},
        {'name': '接入技术类型', 'max':30},
        {'name': '隐藏状态分布', 'max': 20},
        {'name': '释放方分析', 'max': 10},
    ]
    data = {
    'code':200,
    'msg':'success',
    'data':{
        'indicator':indicator,
        'seriesData':seriesData,
        }
    }
    return jsonify(data)

@tel_bp.route('/get_day_count_type',methods=['GET'])
def get_day_count_type():
    sql = "select DATE_FORMAT(event_start_date,'%Y-%m-%d') daytime,procedure_status,count(1) as total from cdr_table group by DATE_FORMAT(event_start_date,'%Y-%m-%d'),procedure_status order by daytime,procedure_status"
    results = query_all(sql)
    days = set()
    data_2G = []
    data_3G = []
    data_4G = []
    data_5G = []
    for item in results:
        days.add(item['daytime'])
        if item['procedure_status'] == 1:
            data_2G.append(item['total'])
        elif item['procedure_status'] == 2:
            data_3G.append(item['total'])
        elif item['procedure_status'] == 3:
            data_4G.append(item['total'])
        else:
            data_5G.append(item['total'])
        day_list = list(days)
        day_list.sort()
    data = {
        'code':200,
        'msg':'success',
        'data':{
            'xAxisData':day_list,
             'dataG':{
                '2G':data_2G,
                '3G':data_3G,
                '4G':data_4G,
                '5G':data_5G
            }
        }
    }
    return jsonify(data)




