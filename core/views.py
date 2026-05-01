from django.shortcuts import render, redirect
from task.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone

User = get_user_model()

@login_required
def dashboard(request):
    users = User.objects.all()
    
    # Admins and Managers see all tasks, regular users see created/assigned tasks
    if request.user.role in ['admin', 'manager']:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(Q(created_by=request.user) | Q(assigned_to=request.user))

    # Calculate overdue status
    today = timezone.now().date()
    for task in tasks:
        task.is_overdue = task.due_date and task.due_date < today and task.status != 'completed'

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'users': users,
    })

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        assigned_id = request.POST.get('assigned_to')
        
        from django.utils.dateparse import parse_date
        due_date_obj = parse_date(due_date)
        
        if due_date_obj and due_date_obj < timezone.now().date():
            from django.contrib import messages
            messages.error(request, "Due date cannot be in the past.")
            return redirect('dashboard')

        assigned_user = User.objects.get(id=assigned_id)
        Task.objects.create(
            title=title, 
            description=description, 
            due_date=due_date, 
            assigned_to=assigned_user,
            created_by=request.user
        )


    return redirect('dashboard')

@login_required
def update_task_status(request, id):

    task = Task.objects.get(id=id)
        # Only creator, assigned user, or admin/manager can update status
    if request.user.role in ['admin', 'manager'] or task.created_by == request.user or task.assigned_to == request.user:
        new_status = request.POST.get('status')
        if new_status in dict(Task.STATUS_CHOICES):
            task.status = new_status
            task.save()
    return redirect('dashboard')

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.user.role in ['admin', 'manager'] or task.created_by == request.user:
        task.delete()

    return redirect('dashboard')