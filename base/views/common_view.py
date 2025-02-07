from django.contrib import messages
from django.db.models import RestrictedError
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView


class CustomDeleteView(DeleteView):

    messages_name = ""

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        error = None
        try:
            self.object = self.get_object()
            self.object.delete()
            messages.info(request, f'{self.messages_name} data successfully deleted with the ID:{kwargs.get('pk')}')
        except RestrictedError as e:
            error = str(e.args[0])
            messages.warning(request, error)
            return HttpResponseRedirect(self.success_url)
        except:
            messages.warning(request, f'No {self.messages_name} record found with the ID:{kwargs.get("pk")}')
            return HttpResponseRedirect(self.success_url)

        return HttpResponseRedirect(self.get_success_url())


class CustomUpdateView(UpdateView):

    messages_name = ""

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        error = None
        try:
            self.object = self.get_object()
            self.object.delete()
            messages.info(request, f'{self.messages_name} data successfully deleted with the ID:{kwargs.get('pk')}')
        except RestrictedError as e:
            error = str(e.args[0])
            messages.warning(request, error)
            return HttpResponseRedirect(self.success_url)
        except:
            messages.warning(request, f'No {self.messages_name} record found with the ID:{kwargs.get("pk")}')
            return HttpResponseRedirect(self.success_url)

        return HttpResponseRedirect(self.get_success_url())