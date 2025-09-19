from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm, ProfileEditForm, CustomPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
<<<<<<< HEAD
            login(request, user)  #  این خط باعث لاگین خودکار می‌شه
            messages.success(request, "Registration was successful and you are logged in.")
=======
            login(request, user)  # 👈 این خط باعث لاگین خودکار می‌شه
            messages.success(request, "ثبت‌نام با موفقیت انجام شد و وارد شدید.")
>>>>>>> 4871b27bece5dc1d3735e1de046b4bef6caf0e49
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
<<<<<<< HEAD


def login_view(request):
    error = None
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")  # یا هر صفحه‌ای که بعد لاگین می‌خوای بره
            else:
                error = "The username or password is incorrect"

    return render(request, "accounts/login.html", {"form": form, "error": error})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')  # یا مسیر صفحه اصلی شما



@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})



class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('profile')
    form_class = CustomPasswordChangeForm 

    def form_valid(self, form):
        messages.success(self.request, "Password changed successfully.")
        return super().form_valid(form)
=======
>>>>>>> 4871b27bece5dc1d3735e1de046b4bef6caf0e49
