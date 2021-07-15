from django.shortcuts import render


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request, *args, **argv):
    return render(request, '500.html', status=500)
