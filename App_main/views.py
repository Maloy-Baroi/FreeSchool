from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from App_main.forms import RoutineUploadForm, ClassVideoUploadForm
from App_main.models import Routine, ClassVideo


# Create your views here.
@login_required
def routine_sys(request):
    exist_routine = Routine.objects.all()  # All information from Routine table
    form = RoutineUploadForm()
    if request.method == 'POST':
        form = RoutineUploadForm(request.POST, request.FILES)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.Author = request.user
            routine.save()
            return HttpResponseRedirect(reverse('App_main:routine'))
    return render(request, 'App_main/Routine.html', context={'form': form, 'Routine': exist_routine})


@login_required
def class_video_sys(request):
    videos = ClassVideo.objects.all()
    form = ClassVideoUploadForm()
    if request.method == 'POST':
        form = ClassVideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            videoForm = form.save(commit=False)
            videoForm.Teacher = request.user
            videoForm.save()
            return HttpResponseRedirect(reverse('App_main:class-videos'))
    return render(request, 'App_main/ClassVideos.html', context={'form': form, 'Videos': videos})
