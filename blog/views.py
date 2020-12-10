from django.shortcuts import render
from django.utils import timezone
from .models import Post, Client
from django.views.generic import TemplateView

# from blog.forms import HomeForm
# class Homeview(TemplateView):
#     template_name = 'blog/index.html'
#
#     def post_list(self, request):
#         # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#         post = Homeview()
#         return render(request, self.template_name, {'form':post})
#
#     def save_client(self, request):
#         form = Homeview(request.POST)
#         if form.is_valid():
#             text = form.cleaned_data['post']
#         args = {'form':form, 'text':text}
#         return render(request, self.template_name, args)

def index(request):
    return render(request, 'blog/index.html', {})

def post_list(request):
    return render(request, 'blog/index.html', {})

def home_page(request):
    name=request.POST["name"]
    tel=request.POST["tel"]
    vin=request.POST["vin"]

    client_info=Client(name=name,tel=tel,vin=vin)
    client_info.save()
    return render(request, 'blog/confirm.html', {})
def save_client(request):
    return render(request, 'blog/index.html', {})


