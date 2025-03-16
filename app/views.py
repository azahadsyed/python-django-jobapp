from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader

from app.models import JobPost

jobTitle = ["First Job", "Second Job", "Third Job",
            "Fourth Job", "Fifth Job", "Sixth Job"]
jobDescription = ["First Job description",  "second job Description", "third job description",
                  "Fourth Job description",  "Fifth job Description", "Dixth job description"]
# Create your views here.
# def hello(Request):
#     return HttpResponse("<h2> Hello World from appOne </h2>")


class TempClass:
    x = 5


def hello(request):
    # template = loader.get_template('app/hello.html')
    itemList = ["Orange", "banana"]
    age = 25
    tempObject = TempClass()
    isAuthenticated = False
    context = {'name': "azahad", 'items': itemList, 'tempObject': tempObject,
               'age': age, 'isAuthenticated': isAuthenticated}
    # return HttpResponse(template.render(context,request))
    return render(request, 'app/hello.html', context)


def jobList(request):
    # listOfJobs = "<ul>"
    # for job in jobTitle:
    #     jobId = jobTitle.index(job)
    #     detailed_url = reverse('jobs_detail',args=(jobId,))
    #     # listOfJobs += f"<li> <a href='job/{jobId}'> {job} </a> </li>"
    #     listOfJobs += f"<li> <a href='{detailed_url}'> {job} </a> </li>"

    # listOfJobs += "</ul>"
    # return HttpResponse(listOfJobs)
    jobs = JobPost.objects.all()
    context = {'jobs': jobs}
    return render(request, 'app/index.html', context)


def jobPage(request, id):
    # return HttpResponse(f"<h1> Hello World from JobPage {id} </h1>")
    print(type(id))
    try:
        if (id == 0):
            # return redirect("/")
            return redirect(reverse('jobs_home'))
        # idAsInt = int(id)
        # htmlMsg = f" <h1> Selected job {jobTitle[idAsInt]} <h1> <h3> Job Description {jobDescription[idAsInt]} </h3>"
        # ----------------------------
        # htmlMsg = f" <h1> Selected job {jobTitle[id]} <h1> <h3> Job Description {jobDescription[id]} </h3>"
        # return HttpResponse(htmlMsg)
        # context = {'jobTitle': jobTitle[id],'jobDescription':jobDescription[id]}
        # return HttpResponse(template.render(context,request))
        jobPost = JobPost.objects.get(id=id)
        context = {'job': jobPost}
        return render(request, 'app/jobdetail.html', context)
    except:
        return HttpResponseNotFound("Not Found...")
