import time
import eventlet
import signal
from skimage import io
import sys

# 调用子进程无法退出
eventlet.monkey_patch()
with eventlet.Timeout(1, False):

    print('ok')
    # img = io.imread('https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train/2884b2f6b1f16a63.jpg')
    img = io.imread('https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train/9452c2879f1585ab.jpg')
    io.imshow(img)
    io.show()
    # time.sleep(40)
    print('没跳过')
print('跳过')

sys.exit()
# linux 使用signal设置装饰器

def time_limit(set_time, callback):
    ''' set_time是设置的时间限制，callback是程序运行后执行的函数 '''

    def wraps(func):
        # 收到信号SIGALRM后的回调函数，参数1是信号的数字，参数2是the interrupted stack frame.
        def handler(signum, frame):
            raise RuntimeError()

        def deco(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(set_time)
            res = func(*args, **kwargs)
            signal.alarm(0)
            return res

        # except RuntimeError as e:
        # callback()  ##如果不想要超时跳转，那么直接删除callback()和对应的参数
        # # print e.message


        return deco
    return wraps


def after_timeout():  # 超时后的处理函数
    print("Time out!")
    return


@time_limit(2, after_timeout)  # 限时 2 秒超时
def connect():  # 要执行的函数
    a = 1
    b = 2
    time.sleep(3)  # 函数执行时间，写大于2的值，可测试超时
    print("完成")
    return a, b


if __name__ == '__main__':
    print("test")
      # 此句正常执行输出
    if time_limit(2, after_timeout) != None: ##如果超时，此步a为None，否则为
        a, b = connect()
        print(a)
          ##正常输出
        print(b)
          ##正常输出
    c = 4
    print(c)
      ##此步正常输出
