#进行users 子应用的视图路由
from django.urls import path
from users.views import RegisterView #导入视图
urlpatterns =[
	#path部分参数1：路由
#到浏览器输入127.0.0.1:8000/register/ 显示视图
	#参数2：视图函数名
	#参数3：路由名，方便通过reverse来获取路由
	path('register/',RegisterView.as_view(),name='register'),
]