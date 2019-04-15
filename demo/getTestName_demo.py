import inspect
# functions
def whoami():
    return inspect.stack()[1][3]
# def whosdaddy():
#     return inspect.stack()[2][3]
# def foo():
#     print("Hello, I'm %s, daddy is %s" % (whoami(), whosdaddy()))
#     bar()
# def bar():
#     print("Hello, I'm %s, daddy is %s" % (whoami(), whosdaddy()))
# johny = bar
# # call them!
# foo()
# bar()
# johny()
def MyFunc():
    x = whoami()
    print(x)

MyFunc()
