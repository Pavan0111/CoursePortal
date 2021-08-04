from django.shortcuts import render, HttpResponse

# Create your views here.
def courseshome(request):
     return render(request, 'courses/courseshome.html')
    #return HttpResponse('This is courseshome. We wiil keep all the courses here')

def coursesPost(request, slug):
     return render(request, 'courses/coursesPost.html')
    #return HttpResponse(f'This is coursesPost: {slug}')

