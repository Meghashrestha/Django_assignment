from django.shortcuts import render,redirect
from .models import Blogdetails, Writername
from .forms import Form
from django import template

from django.http import HttpResponse

# class ModelView(ListView):
#     model = Entry
#     template_name = 'entries/index.html'
def index(request):
    return render(request, 'index.html',{})


def post(request):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            # print((request.POST))
            form.save()
            print("hi")
            return redirect('/post/')
        else:
            return HttpResponse("sth wrong")
    return render(request, 'post.html', {})
def submit(request):
    print("hiii")
    return render(request, 'post.html', {})

# def blog(request):
#     return render(request,'blog.html',{})

def itemview(request):
    # userdata = Writerdetail.objects.all()
    data = Blogdetails.objects.all()
    # data1 = Blogdetails.writer_name()
    # name = Writername.objects.all()
    return render(request,'blog.html', {'data': data})
# def itemview(request, writer):
#     title = [t.blog_title for t in Writername.objects.all()]
#     if writer in title:
#         return HttpResponse(f"{writer} is a writer")
#     blog_title = [t.blog_title]
#
#     # userdata = Writerdetail.objects.all()
#     # data = userdata.Blogdetails.get(userdata)
#     return render(request,'blog.html', {'data': data})
# def blog(request):
#     return render(request, 'blog.html', {"blog_title": Writername.objects.all})
# def singleblog(request, single_blog):
#     blog_title =[b.blog_title for b in Writername.objects.all()]
#     if single_blog in blog_title:
#         series_urls = {}
#         matching_series = Writername.objects.filter(writername__writer_name=single_blog)
#         for m in matching_series.all():
#             part_one = Blogdetails.objects.filter(writername__writername=m.Writername).earliest(
#                 "Published")
#             series_urls[m] = part_one.blog
#             return render(request, 'blog.html',{'blog_title': matching_series, 'part_ones': series_urls})



