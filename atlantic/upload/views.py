from django.http import HttpResponseRedirect

#Redirect all index requests to admin page
def index(request):
    return HttpResponseRedirect('/upload')
