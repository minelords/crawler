from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import JsonResponse
# Create your views here.
class Aview(TemplateView):
    template_name='a.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': "<iframe src='https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php' style='width: 100%; height:600px; border: none;'></iframe>"  # 将参数传递给模板
        }
        return render(request, self.template_name, context)

    
    
class Bview(TemplateView):
    template_name='b.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': "<iframe src='https://iframe.arkoselabs.com/3EE79F8D-13A6-474B-9278-448EA19F79B3/index.html' style='width: 100%; height:600px; border: none;'></iframe>"  # 将参数传递给模板
        }
        return render(request, self.template_name, context)
    
class Cview(TemplateView):
    template_name='c.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': "<iframe src='https://castatic.fengkongcloud.cn/pr/v1.0.4/demo.html' style='width: 100%; height:600px; border: none;'></iframe>"  # 将参数传递给模板
        }
        return render(request, self.template_name, context)
    
class Dview(TemplateView):
    template_name='d.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': "<iframe src='https://castatic.fengkongcloud.cn/pr/v1.0.4/select/seq_select.html' style='width: 100%; height:600px; border: none;' ></iframe>"  # 将参数传递给模板
        }
        return render(request, self.template_name, context)
    
class Eview(TemplateView):
    template_name='e.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': "<iframe src='/generic/mathcaptcha' style='width: 100%; height:600px; border: none;' ></iframe>"  # 将参数传递给模板
        }
        return render(request, self.template_name, context)
    
class Fview(TemplateView):
    template_name='f.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': '<iframe src="/generic/log" style="width: 100%; height:600px; border: none;"></iframe>'  # 将参数传递给模板
        }
        return render(request, self.template_name, context)
    
    
class Gview(TemplateView):
    template_name='g.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': "<iframe src='https://castatic.fengkongcloud.cn/pr/v1.0.4/select/spatial_select.html' style='width: 100%; height:600px; border: none;' ></iframe>"  # 将参数传递给模板
        }
        return render(request, self.template_name, context)