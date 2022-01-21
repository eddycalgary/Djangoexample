from django.shortcuts import render, redirect
from functools import lru_cache

# Create your views here.
# def HOME(request):
#     print(request.method)
#     return render(request, 'Home.html')



def testform(request):
    if request.method=='POST':
        if "fname" in request.POST:
            print("Name found")
        print(request.method)
        x = request.POST.get('fname')
        print(x)
        #z = int(request.POST.get('fname'))
        tlist = []
        #for i in range(z):
        #    tlist.append(fib(i))
        # selected_project = x
        # request.session['selected_project'] = selected_project
        print(tlist)
        print(len(tlist))
        #content = request.POST['test']
        return render(request, 'answer.html', {'content': x})

    elif request.method == "GET":
        return render(request, 'Home.html')

def test(request):
    if request.method == 'GET':
        # selected_project_id = request.session.get('selected_project_id')
        return render(request, 'about.html', {'test': "This is page about"})


@lru_cache(maxsize=10)
def fib(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

