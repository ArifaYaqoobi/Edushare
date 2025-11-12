from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Resource, Subject, GradeLevel
from .forms import ResourceForm, CommentForm

def index(request):
    subjects = Subject.objects.all()
    grades = GradeLevel.objects.all()
    resources = Resource.objects.order_by('-created_at')[:20]
    return render(request, 'main/index.html', {
        'resources': resources,
        'subjects': subjects,
        'grades': grades,
    })

def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    comment_form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.resource = resource
            comment.save()
            return redirect('main:resource_detail', pk=pk)
    return render(request, 'main/resource_detail.html', {
        'resource': resource,
        'comment_form': comment_form,
    })

@login_required
def resource_add(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.owner = request.user
            resource.save()
            return redirect('main:index')
    else:
        form = ResourceForm()
    return render(request, 'main/resource_add.html', {'form': form})

def api_search(request):
    # AJAX endpoint: ?q=term&subject=1&grade=2
    q = request.GET.get('q','').strip()
    subject = request.GET.get('subject')
    grade = request.GET.get('grade')
    queryset = Resource.objects.all().order_by('-created_at')
    if q:
        queryset = queryset.filter(title__icontains=q)
    if subject:
        queryset = queryset.filter(subject_id=subject)
    if grade:
        queryset = queryset.filter(grade_id=grade)
    results = []
    for r in queryset[:50]:
        results.append({
            'id': r.id,
            'title': r.title,
            'subject': r.subject.name if r.subject else '',
            'grade': r.grade.name if r.grade else '',
            'owner': r.owner.username,
            'created_at': r.created_at.strftime('%Y-%m-%d'),
        })
    return JsonResponse({'results': results})
