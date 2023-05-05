# from django.shortcuts import render,redirect
# from .forms import SignUpForm
# from .models import Profile
# from django.contrib.auth import authenticate, login
# # Create your views here.

# def SignUp(request):
#     if request.method=='POST':
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user=authenticate(username=username,password=password)
#             login(request,user)
#             return redirect('/accounts/profile')
#     else:
#         form=SignUpForm()
        
    
#     return render(request,'registration/signup.html',{'form':form})
    
    
# def my_profile(request):
#     profile=Profile.objects.get(user=request.user)
#     return render(request,'profile/profile.html',{'profile':profile})
    
    