from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import bookshop, PostImage, Category, Contact
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from market.forms.forms_ex import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from .my_captcha import FormWithCaptcha
import requests
# Create your views here.


def home(request):
    # แสดงประเภทสินค้าทั้งหมด
    all_category = Category.objects.all().filter(categoty_activate="True")
    # เรียงตามชื่อ
    categories = all_category.order_by('category_name')

    # เลือกเฉพาะสถานะ Active
    recommend = bookshop.objects.filter(book_active="True", book_recommend="True")
    # แถบ Category ที่ Navbar
    category = Category.objects.all()
    paginator = Paginator(recommend, 4)
    page = request.GET.get('page')
    try:
        recommend = paginator.page(page)
    except PageNotAnInteger:
        recommend = paginator.page(1)
    except EmptyPage:
        recommend = paginator.page(paginator.num_pages)
    
    book = recommend
    
    context = {
        'book': book,
        'category': category,
        'categories': categories,
    }
    return render(request, 'home.html', context)


def recommend(request):
    # เลือกเฉพาะสถานะ Active
    recommend = bookshop.objects.filter(
        book_active="True", book_recommend="True")
    
    paginator = Paginator(recommend, 4)
    page = request.GET.get('page')
    try:
        recommend = paginator.page(page)
    except PageNotAnInteger:
        recommend = paginator.page(1)
    except EmptyPage:
        recommend = paginator.page(paginator.num_pages)
    
    book = recommend
    context = {
        'book': book,
        'recommend': recommend,
    }
    return render(request, 'product/recommend.html', context)


def show_app_product(request):
    book = bookshop.objects.all().filter(book_active="True")
    category = Category.objects.all()

    context = {
        'book': book,
        'category': category,

    }
    return render(request, 'product/allproduct.html', context)


def category_select(request, pk):
    book = bookshop.objects.filter(book_category_id=pk)

    # เรียงตามราคา
    book = book.order_by('book_price').filter(book_active="True")

    context = {
        'book': book,
        'category': category,
        'text_search': text_search,
        'info': info,
        'title': title,

    }
    return render(request, 'product/category_select.html', context)


def category(request, pk):
    book = bookshop.objects.filter(book_category_id=pk)

    # เรียงตามราคา
    book = book.order_by('book_price').filter(book_active="True")

    # แถบ Category ที่ Navbar
    category = Category.objects.all()
    # Title
    title = category.get(pk=pk)
    # Search
    text_search = request.GET.get('text_search', "")
    sort = request.GET.get('sort', 'desc')
    if sort == 'desc':
        book = book.order_by('-book_price')
        info = "ราคา : เรียงจากมากไปน้อย"
    else:
        book = book.order_by('book_price')
        info = "ราคา : เรียงจากน้อยไปมาก"

    paginator = Paginator(book, 4)
    page = request.GET.get('page')
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)
    context = {
        'book': book,
        'category': category,
        'text_search': text_search,
        'info': info,
        'title': title,

    }
    return render(request, 'category.html', context)


def show_app_product(request):
    book = bookshop.objects.all().filter(book_active="True")
    category = Category.objects.all()

    context = {
        'book': book,
        'category': category,

    }
    return render(request, 'product/allproduct.html', context)


def all(request):
    book = bookshop.objects.all()
    category = Category.objects.all()

    text_search = request.GET.get('text_search', "")
    if text_search != "":
        book = bookshop.objects.filter(Q(book_name__icontains=text_search))
    else:
        book = bookshop.objects.all().filter(book_active="True")

    sort = request.GET.get('sort', 'desc')
    if sort == 'desc':
        book = book.order_by('-book_price')
        info = "ราคา : เรียงจากมากไปน้อย"
    else:
        book = book.order_by('book_price')
        info = "ราคา : เรียงจากน้อยไปมาก"

    paginator = Paginator(book, 4)
    page = request.GET.get('page')
    try:
        book = paginator.page(page)
    except PageNotAnInteger:
        book = paginator.page(1)
    except EmptyPage:
        book = paginator.page(paginator.num_pages)

    context = {
        'book': book,
        'category': category,
        'text_search': text_search,
        'sort': sort,
        'info': info,
    }
    return render(request, 'allcategory.html', context)


def detail_view(request, pk):
    post = get_object_or_404(bookshop, pk=pk)
    data = get_object_or_404(bookshop, pk=pk)
    photos = PostImage.objects.filter(post=post)
    rec = bookshop.objects.filter(book_active="True")
    category = Category.objects.all()
    return render(request, 'detail.html', {
        'data': data,
        'post': post,
        'photos': photos,
        'category': category,
        'rec': rec,
    })

def product_detail_2(request,pk):
    post = get_object_or_404(bookshop, pk=pk)
    data = get_object_or_404(bookshop, pk=pk)
    photos = PostImage.objects.filter(post=post)
    recommend = bookshop.objects.filter(book_active="True", book_recommend="True")
    category = Category.objects.all()
    paginator = Paginator(recommend, 4)
    page = request.GET.get('page')
    try:
        recommend = paginator.page(page)
    except PageNotAnInteger:
        recommend = paginator.page(1)
    except EmptyPage:
        recommend = paginator.page(paginator.num_pages)
    book = recommend
    context = {
        'data': data,
        'post': post,
        'photos': photos,
        'category': category,
        'book': book,
    }
    return render(request, 'productdetail.html',context) 

@csrf_exempt
def contact_view(request):
    category = Category.objects.all()
    form = ContactForm(request.POST)
    if request.method == 'POST':
        token = request.POST.get('g-recaptcha-response')
        secret = requests.post('https://www.google.com/recaptcha/api/siteverify', {
                               'secret': '6LdrzjQbAAAAAHxs1xcLkgeaRZX71o53aK12UNES', 'response': token})
        print(secret.json()['success'])
        if secret.json()['success']:
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Message Sended', 'success')
        else:
            messages.add_message(request, messages.ERROR, 'Error', 'danger')
    form = ContactForm()
    context = {
        'form': form,
        'category': category,
        'captcha': FormWithCaptcha,
    }
    return render(request, 'contact.html', context)


def nav_category(request):
    data = Category.objects.all()
    text_search = request.GET.get('text_search', "")
    sort = request.GET.get('sort', 'desc')
    context = {
        'data': data,
        'text_search': text_search,
        'sort': sort,
    }
    return render(request, 'layout/base.html', context)


def pageination(request):
    data = Category.objects.all()
    text_search = request.GET.get('text_search', "")
    sort = request.GET.get('sort', 'desc')
    context = {
        'data': data,
        'text_search': text_search,
        'sort': sort,
    }
    return render(request, 'layout/pagination.html', context)


def about(request):
    category = Category.objects.all()
    data = Category.objects.all()
    recommend = bookshop.objects.filter(book_active="True", book_recommend="True")
    text_search = request.GET.get('text_search', "")
    sort = request.GET.get('sort', 'desc')
    context = {
        'data': data,
        'text_search': text_search,
        'sort': sort,
        'category': category,
        'recommend':recommend,
    }
    return render(request, 'about.html', context)


