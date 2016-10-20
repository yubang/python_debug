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
    a7()


def a7():
    b = 100
    c = 0
    return b / c


if __name__ == '__main__':
    debugger.set_throw_error(False)
    debugger.run_func(a1, {})
