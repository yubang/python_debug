# coding:UTF-8


"""
调试器核心程序
@author: yubang
"""


from object_handler import get_object_all_data
import sys
import json
import traceback


class Debugger:
    def __init__(self):
        self.__output_func = self.__print
        self.__throw_error = True

    def __get_data_from_frame(self, frame):
        """
        根据frame获取当前作用域内信息
        :param frame:
        :return:
        """
        d = {
            "filepath": frame.tb_frame.f_code.co_filename,
            "code_line": frame.tb_lineno,
            "data": []
        }
        for k in frame.tb_frame.f_locals:
            d['data'].append(get_object_all_data(frame.tb_frame.f_locals[k], k))
        return d

    def __get_all_func_data_arr(self, e):
        """
        获取所有函数内变量
        :param e: 错误对象
        :return:
        """
        arr = []
        frame = sys.exc_info()[2]
        while True:
            if not hasattr(frame, "tb_next"):
                break
            arr.append(self.__get_data_from_frame(frame))
            frame = frame.tb_next
        return {"trace": arr, "error": traceback.format_exc(), "e": repr(e)}

    @staticmethod
    def __print(message):
        """简单打印输出"""
        print json.dumps(message, indent=2, ensure_ascii=False)

    def set_output_func(self, func):
        """
        设置输出函数
        :param func: 函数
        :return:
        """
        self.__output_func = func

    def set_throw_error(self, b):
        """
        设置是否抛出异常
        :param b: 是否抛出异常
        :return:
        """
        self.__throw_error = b

    def run_func(self, func, func_param_dict):
        """
        执行入口函数
        :param func: 函数
        :param func_param_dict: 参数字典
        :return:
        """
        try:
            return func(**func_param_dict)
        except Exception, e:
            obj = self.__get_all_func_data_arr(e)
            self.__output_func(obj)
            if self.__throw_error:
                raise
