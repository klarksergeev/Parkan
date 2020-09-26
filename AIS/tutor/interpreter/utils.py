from django.shortcuts import render

class ObjectDetailMixin:
    template = None

    def get(self, request):
        return render(request, self.template)