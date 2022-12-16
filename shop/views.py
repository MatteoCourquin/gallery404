from .forms import ArticleForm
from .models import ArticleModel
from django.shortcuts import render
from django.shortcuts import render


def index(request):
    context = {
        'products': ArticleModel.objects.all()
    }
    return render(request, 'shop/index.html', context)


def create_view(request):

    context = {}

    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "shop/create_view.html", context)


def detail_view(request, id):

    context = {}

    context["product_detail"] = ArticleModel.objects.get(id=id)

    return render(request, "shop/detail_view.html", context)
