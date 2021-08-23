from django.conf.urls import url
from django.http import HttpResponse

def Products(request):
    return HttpResponse('<body bgcolor="blue"> Welcome to the Products page<br></body>')
def Mobiles(request):
    return HttpResponse('<body bgcolor="blue"> Welcome to the Mobile page<br></body>')
def Books(request):
    return HttpResponse('<body bgcolor="blue"> Welcome to the Books page<br></body>')

def Test1(request):
    return HttpResponse('<body bgcolor="blue"> This is Test1 from Blog app<br></body>')

from django.shortcuts import render

def Hellotemplate(request):
    context={}
    return render(request,"hello.html",context)

def Products(request):
    context={'proddb': [
        {'pid':101,'pname':'Dive into python3','price':450,'author':'Milton'},
        {'pid':102,'pname':'Python algorithms','price':550,'author':'Charles'},
        {'pid':103, 'pname': 'Networking python', 'price': 650, 'author': 'Miller'},
        {'pid': 104, 'pname': 'Advanced python', 'price': 350, 'author': 'Robert'},
        {'pid': 105, 'pname': 'Python for automation', 'price': 367, 'author': 'Smith'}
    ]}
    return render(request,"prodsmultiple.html",context)

# Creating a table in DB by creating models and displaying that table to user using blog_data.html template
from .models import Post
def posts(request):
    context={'blogdb':Post.objects.all()} #sending the data in a Model into context/template
    return render(request,'blog_data.html',context)
# Calling the template which is created inside the app (blog/templates/blog/test.html)
def blogTest(request):
    context={}
    return render(request,'blog/test.html',context)
# Creating a form and sending the form to email once it is filled (No model is created)
from .form import ContactForm
from django.shortcuts import HttpResponseRedirect
from django.core.mail import EmailMessage

def Thanks(request):
    context={}
    return render(request,'blog/thankyou.html',context)


def Contact(request):  # <==========added

    # GET REQUEST
    form_class = ContactForm  # class not a instance
    context = {'form': form_class}

    # POST REQUEST
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            phno = form.cleaned_data['phno']
            content = form.cleaned_data['text']
            subject = f"A new contact or lead - {contact_name}"
            email = EmailMessage(subject, contact_name + '\n' + contact_email + '\n' + str(phno) + '\n' + content,
                                 to=['ajaygudekal81@gmail.com'])
            email.send()

            return HttpResponseRedirect('/blog/thanks/')  # project-url/app-url
    return render(request, 'blog/blog_contact.html', context)

# Creating a form, storing all the form once it is filled to the database by creating Models
from .form import EnqDBForm
from .models import EnqDB
def StudentInsert(request):

    if request.method=="POST":
        form=EnqDBForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            mail=form.cleaned_data['mail']
            mno=form.cleaned_data['mno']
            messege=form.cleaned_data['messege']
            EnqDB.objects.create(name=name,mail=mail,mno=mno,messege=messege)
            return HttpResponseRedirect('/blog/thanks/')
        else:
            context={'form':form}
            return render(request,'blog/contactform.html',context)
    else:
        form=EnqDBForm
        context={'form':form}
        return render(request,'blog/contactform.html',context)

from .form import Postform
from .models import Postlu

def Postablog(request):

    if request.method == 'POST':
        form=Postform(request.POST)

        if form.is_valid():
            author=form.cleaned_data['author']
            title=form.cleaned_data['title']
            text=form.cleaned_data['text']
            created_date=form.cleaned_data['created_date']
            Postlu.objects.create(author=author,title=title, text=text,created_date=created_date)
            subject=f"Hey Ajay!, {author} has created a New blog on your Website"

            email=EmailMessage(subject, author + '\n' + title + '\n', to=['ajaygudekal81@gmail.com'])
            email.send()

            return HttpResponseRedirect('/blog/thanks/')

        else:
            context={'form':form}
            return render(request,'blog/postablog.html',context)
    else:
        form=Postform
        context={'form':form}
        return render(request,'blog/postablog.html',context)


def Home(request):
    context={'blogdb':Postlu.objects.all()}
    return render(request,'home.html',context)

def AboutUs(request):
    context={}
    return render(request,'blog/aboutus.html',context)




