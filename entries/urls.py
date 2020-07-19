from django.urls import path
from .views import index,post, itemview

urlpatterns = [
    path('', index),
    path('post/', post),
    # path('blog/', singleblog, name = 'single_blog'),
    path('blog/', itemview),

    # path('', ),
    # path('home/', ModelView.as_view(), name = 'blog-home'),

]
