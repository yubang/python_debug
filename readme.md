### 简单的python debug辅助小工具

开发本插件的起因：线上错误无法重现，如果出错的时候记录下所有函数调用过程的变量数据，那么就可以更好的分析错误原因！


### 使用方法（可以参考demo.py文件）


```
# coding:UTF-8


from debugger import debugger


def a1():
    a2()


def a2():
    a3()


def a3():
    a4()


def a4():
    a5()


def a5():
    a6()


def a6():
    a = 5
    a7()


def a7():
    b = 100
    c = 0
    return b / c


if __name__ == '__main__':
    debugger.set_throw_error(False)
    debugger.run_func(a1, {})

```

总的来说，引入debugger对象，然后传递要执行的函数即可。


### debugger对象函数说明

set_throw_error(是否抛出出错函数<bool>) # 设置是否抛出错误

run_func(需要执行的函数, 参数字典) # 执行函数

set_output_func(结果处理函数) # 设置处理出错时捕捉到的所有数据（该函数接收一个参数，捕捉数据对象）


### 捕捉数据对象（结构如下图）


```
{
    "e": 出错信息,
    "error": 错误栈堆字符串,
    trace: [

         {
          "func_name": "函数名",
          "data": [
              "type": "变量类型",
              "name": "变量名字",
              "value": 如果是基本类型，则为数值，如果是字典或者对象或者列表，则为像data这样子的字典（下面以此类推）
          ],
          "code_line": 函数在文件第几行,
          "filepath": "文件路径"
        },...

    ]
}

```


### 在线解释捕捉到的数据对象

打开网址：<a href="http://htmlpreview.github.io/?https://github.com/yubang/python_debug/blob/master/web/index.html">http://htmlpreview.github.io/?https://github.com/yubang/python_debug/blob/master/web/index.html</a>

在网页粘贴数据对象字符串，然后点击分析，然后可以点击分析即可。


<img src="http://p1.bqimg.com/4851/2977f367434e5431.png" />
