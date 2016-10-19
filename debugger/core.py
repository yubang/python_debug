# coding:UTF-8


"""
调试器核心程序
@author: yubang
"""


import sys


class Debugger:
    def __init__(self):
        self.__output_func = self.__print


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
            d['data'].append({
                "name": k,
                "type": type(frame.tb_frame.f_locals[k]).__name__,
                "value": frame.tb_frame.f_locals[k]
            })
        return d

    def __get_all_func_data_arr(self):
        """
        获取所有函数内变量
        :return:
        """
        arr = []
        frame = sys.exc_info()[2]
        while True:
            if not hasattr(frame, "tb_next"):
                break
            arr.append(self.__get_data_from_frame(frame))
            frame = frame.tb_next
        return arr

    @staticmethod
    def __print(message):
        """简单打印输出"""
        print message

    def run_func(self, func, func_param_dict):
        """
        执行入口函数
        :param func: 函数
        :return:
        """
        try:
            return func(**func_param_dict)
        except Exception:
            obj = self.__get_all_func_data_arr()
            self.__output_func(obj)
            raise
