# coding:UTF-8


"""
对象转可序列化模块
@author: yubang
"""


from datetime import datetime, time, date
from collections import Iterable
import types


def get_object_all_data(obj, name=None, deep=0, max_deep=50):
    """获取类对象所有数据"""
    d = {
        "name": name,
        "type": type(obj).__name__,
        "value": None
    }
    if deep > max_deep:
        d['value'] = "由于层数限制无法获取数据"
        return d

    if isinstance(obj, (str, int, float, bool)):
        d['value'] = obj
    elif isinstance(obj, unicode):
        # d['type'] = 'str'
        # d['value'] = obj.encode("UTF-8")
        d['value'] = obj
    elif obj is None:
        d['value'] = obj
    elif isinstance(obj, datetime):
        d['value'] = obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, date):
        d['value'] = obj.strftime("%Y-%m-%d")
    elif isinstance(obj, time):
        d['value'] = obj.strftime("%H:%M:%S")
    elif isinstance(obj, dict):
        d['value'] = []
        for k in obj:
            d['value'].append(get_object_all_data(obj[k], k, deep=deep + 1, max_deep=max_deep))
    elif isinstance(obj, (list, Iterable)):
        d['value'] = []
        for data in obj:
            d['value'].append(get_object_all_data(data, deep=deep + 1, max_deep=max_deep))
    elif hasattr(obj, "__call__"):
        d['value'] = repr(obj)
    elif type(obj).__name__ == 'module':
        d['value'] = repr(obj)
    else:
        d['value'] = []
        obj_dir_datas = dir(obj)
        for k in obj_dir_datas:
            try:
                if not k.startswith("__") and (type(getattr(obj, k)) in (types.InstanceType, types.ClassType) or isinstance(getattr(obj, k), (str, unicode, bool, int, float, type(None)))):
                    d['value'].append(get_object_all_data(getattr(obj, k), k, deep=deep+1, max_deep=max_deep))
            except AttributeError:
                pass

    return d
