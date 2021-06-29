from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegistrationForm, AboutUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        a_form = AboutUpdateForm(request.POST, instance=request.user.about)
        if u_form.is_valid() and p_form.is_valid() and a_form.is_valid():
            u_form.save()
            p_form.save()
            a_form.save()
            messages.success(request, 'Your account has been updated successfully!')
            return redirect('profile')
        else:
            messages.warning(request, 'Please correct the error below.')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        a_form = AboutUpdateForm(instance=request.user.about)

    context = {
        'u_form': u_form,
        'a_form': a_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


