from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    phones = Phone.objects.all()

    phones_list = []
    for device in phones:
        phones_list.append({
            'name': device.name,
            'price': round(device.price),
            'image': device.image,
            'slug': device.slug
        }
        )

    if request.GET.get('sort'):
        sort = request.GET.get('sort')
        if sort == 'name':
            phones_list.sort(key=lambda val: val['name'])
        elif sort == 'min_price':
            phones_list.sort(key=lambda val: val['price'])
        elif sort == 'max_price':
            phones_list.sort(key=lambda val: val['price'], reverse=True)
        else:
            pass

    context = {
        'phones_list': phones_list,
    }

    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    release_date = phone.release_date.strftime('%d.%m.%Y')

    if phone.lte_exists:
        lte = 'есть'
    else:
        lte = 'отсутствует'
    info = {
        'name': phone.name,
        'price': round(phone.price),
        'image': phone.image,
        'release_date': release_date,
        'lte': lte
    }
    context = {
        'phone': phone,
        'phone': info
    }

    return render(request, template, context)