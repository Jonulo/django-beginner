from django.shortcuts import render, redirect
from datetime import datetime

# django para validar si hay alguna sesión abierta
from django.contrib.auth.decorators import login_required

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm
posts_hardcode = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/60/60?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036',
    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/60/60?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo Auditorio',
        'user': {
            'name': 'Thespianartist',
            'picture': 'https://picsum.photos/60/60?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

# Url a donde redirijir está definida en setting.py
@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    
    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    
    return render(
        request =request,
        template_name ='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
# De esta forma implementamos datos de forma rapida dentro de HTML:
# ----- 
# def list_posts(request):
#    content = []
#    for post in posts:
#        content.append("""
#            <p><strong>{name}</strong></p>
#           <p><small>{user} - <i>{timestamp}</i></small></p>
#            <figure><img src="{picture}"></figure>
#       """.format(**post))
#    return HttpResponse('<br>'.join(content))
