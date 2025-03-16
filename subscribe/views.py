from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.


def subscribe(request):
    emailErrorEmpty = ""
    subscribeForm = SubscribeForm()
    if request.POST:
        # firstName = request.POST['firstName']
        # lastName = request.POST['lastName']
        # emailId = request.POST['email']
        subscribeForm = SubscribeForm(request.POST)
        if subscribeForm.is_valid():
            # print("This is a Valid Form...")
            # print(subscribeForm.cleaned_data)
            # firstName = subscribeForm.cleaned_data['firstName']
            # lastName = subscribeForm.cleaned_data['lastName']
            # emailId = subscribeForm.cleaned_data['emailId']
            # print(emailId, firstName, lastName)
            # subscribeForm = Subscribe(
            #     firstName=firstName, lastName=lastName, emailId=emailId)
            subscribeForm.save()
            return redirect(reverse('thank_you'))
        # print("POST Request...",emailId, firstName, lastName)
        # # collect the email , check blank or not
        # if emailId == "":
        #     emailErrorEmpty = "No Email Entered..."
        else:
            print("Form is not valid")
            print(subscribeForm.errors)

    context = {"InputForm": subscribeForm, "emailErrorEmpty": emailErrorEmpty}
    # context = {"forms":subscribeForm}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)
