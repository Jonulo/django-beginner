from django.shortcuts import render
from datetime import datetime

posts = [
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
def list_posts(request):
    return render(request, 'feed.html', {'posts': posts})

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
