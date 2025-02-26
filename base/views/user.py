from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from base.forms.user import UserForm, UserUpdateForm
from base.views.common_view import CustomDeleteView


# List Users View (Read)
class UserListView(TemplateView):
    template_name = 'user.html'

    def post(self, request, *args, **kwargs):
        new = True
        form = UserForm(self.request.POST)
        user_id = request.POST.get('user_id')
        if user_id:
            user = get_object_or_404(User, pk=user_id)
            form = UserUpdateForm(request.POST, instance=user)
            new = False

        if form is not None and form.is_valid():
            data = form.save(commit=False)
            password = request.POST.get('password1')
            if password:
                data.password = make_password(password)
            data.save()
            if new:
                messages.success(request, f'User successfully created with the ID: {data.pk}')
            else:
                messages.info(request, f'User successfully updated with the ID: {data.pk}')
        elif form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f'{field}: {error}')

        return redirect('user-home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['form'] = UserForm()
        # Fetch all users
        return context

class UserDelete(CustomDeleteView):
    model = User
    messages_name = "User"
    success_url = reverse_lazy("user-home")
