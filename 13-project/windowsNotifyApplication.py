#install: "pip install win10toast"

from win10toast import ToastNotifier
import datetime

data = datetime.datetime.now()
data = str(data)

toaster = ToastNotifier()
toaster.show_toast("Hello World!!!",
"Python is 10 seconds!",
icon_path="custom.ico",
duration=10)

toaster.show_toast("Date-Time Update", data, icon_path=None, duration=10)



