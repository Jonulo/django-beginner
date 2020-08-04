from django.http import HttpResponse
import json

def get_numbers(request):
    nums = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(nums)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(json.dumps(data, indent=4),
    content_type='application/json')

def test(request, name, age):
    if age < 15:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Welcome {} to jonugram!'.format(name)
    
    return HttpResponse(message)