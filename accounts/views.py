from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return  redirect('login')       
    else:
        return render(request,'login.html')



def register(request):
    #get data from html
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            #check username records which user entered in database is already exist or not
            if User.objects.filter(username=username).exists():
                print("User Name Taken")
                messages.info(request,'User Name Taken')
                return redirect('register')
            #check email records which user entered in database is already exist or not
            elif User.objects.filter(email=email).exists():
                print("Email Taken")
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
            #create objnect with values of html as parameters
            #and send to database using User.objects.create_user()method
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            print('Password not matched')
            return redirect('register')
        #redirect to home page
        return redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
