from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import misaka
from django.utils.text import slugify
from cabinet.models import Note, Tag
from cabinet.forms import NoteForm, TagForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def note_list(request, template_name='cabinet/note_list.html'):
    data = Note.objects.all().filter(user=request.user).order_by('-created')
    notes = {}
    notes['object_list'] = data
    data_t = Tag.objects.all().filter(user=request.user).order_by('user_tag')
    tags = {}
    tags['object_list'] = data_t

    paginator = Paginator(data, 7)
    try:
        page = request.GET.get('page')
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        page = paginator.page(paginator.num_pages)
    try:
        note_list = paginator.page(page)
    except:
        note_list = paginator.page(paginator.num_pages)

    request.session['cabinet'] = True
    return render(request, template_name, {'note_list': note_list,
                                          'tags':tags})

def note_create(request, template_name='cabinet/note_new.html'):
    form = NoteForm(request.POST or None)
    data = Tag.objects.all().filter(user=request.user).order_by('user_tag')
    tags = {}
    tags['object_list'] = data

    if form.is_valid():
        print("And the form is valid")
        instance = form.save(commit=False)
        instance.user = request.user
        instance.htmltext = misaka.html(instance.text)
        instance.slug = slugify(instance.title)
        instance.text_tag = tag_fest(instance.text_tag).lower()
        instance.save()
        tag_updateDB(tag_fest(instance.text_tag), instance.user)

        # return redirect('cabinet:note_list')
        return redirect('/fc/?page=1')
    return render(request, template_name, {'form':form,'tags':tags})

def note_update(request, pk, template_name='cabinet/note_form.html'):
    data = Tag.objects.all().filter(user=request.user).order_by('user_tag')
    tags = {}
    tags['object_list'] = data
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.text_tag = tag_fest(instance.text_tag).lower()
        instance.save()
        tag_updateDB(tag_fest(instance.text_tag), instance.user)
        # return redirect('cabinet:note_list')
        return redirect('/fc/?page=1')
    return render(request, template_name, {'form':form,'tags':tags})

def tag_updateDB(tags,iuser):
    tag_list=tags.split(',')
    for i in range(len(tag_list)):
        Tag.objects.get_or_create(user_tag=tag_list[i], user=iuser)

def tag_fest(tags):
    tag_list = tags.split(',')
    for i in range(len(tag_list)):
        tag_list[i] = slugify(tag_list[i])
    return ','.join(tag_list)

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method=='POST':
        note.delete()
        return redirect('cabinet:note_list')
    return redirect('cabinet:note_list')

def tag_create(request, template_name='cabinet/tag_new.html'):
    data = Tag.objects.all().filter(user=request.user).order_by('user_tag')
    tags = {}
    tags['object_list'] = data

    form = TagForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.user_tag = instance.user_tag.lower()
        instance.save()

        return redirect('cabinet:note_list')
    # Add TAGs to Args
    return render(request, template_name, {'form':form,
                                            'tags':tags})
