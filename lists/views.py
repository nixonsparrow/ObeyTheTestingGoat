from django.shortcuts import render, redirect
from django.views.generic import DetailView
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(list=list_, text=request.POST['item_text'])
    return redirect(f'/lists/{list_.id}/')


class SingleListView(DetailView):
    model = List
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        return {
            'list': self.get_object(),
            # 'items': Item.objects.filter(list=self.get_object()),
        }
