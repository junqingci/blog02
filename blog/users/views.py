from django.shortcuts import render

# Create your views here.
from django.views import View
#注册视图
class RegisterView(View):  #标红导入View解决后出现上部分
	def get(self,request):

		return render(request,'register.html')