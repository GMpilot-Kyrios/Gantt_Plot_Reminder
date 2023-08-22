from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

# 有icon的版本
toaster.show_toast("Hello World!!!",
                   "Python is 10 seconds awsm!")

# 无icon，采用python的icon，且采用自己的线程
toaster.show_toast("Example two",
                   "This notification is in it's own thread!",
                   threaded=True)

# 等待提示框关闭
while toaster.notification_active(): time.sleep(0.1)