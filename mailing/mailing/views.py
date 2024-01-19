from .models import Client, Mailing

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View


class MailDistribution(View):
    def send_mailing(request, mailing_id):
        try:
            mailing = Mailing.objects.get(id=mailing_id)
            clients = Client.objects.filter(
                    operator_code=mailing.client_filter_operator_code,
                    tag=mailing.client_filter_tag)
        except Mailing.DoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'A message id doesn\'t exist',
                                 'code': 0})
        except Client.DoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'A client doesn\t exist',
                                 'code': 0})
        # send message
        for client in clients:
            # We send client.phone_number with mailing_id.message
            # As sample: requests.post(url, data)
            pass
        return JsonResponse({'status': 'success',
                             'code': 1})

    def cancel_mailing(request, mailing_id):
        try:
            mailing = Mailing.objects.get(id=mailing_id)
            mailing.end_datetime = mailing.start_datetime
            mailing.save()
        except Mailing.DoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'Send messages doesn\'t canceling.\
 message id doesn\'t exist', 'code': 0})
        return JsonResponse({'status': 'success',
                             'message': 'Send messages canceling',
                             'code': 1})

    @csrf_exempt
    def upload_data(request):
        if request.method == 'POST':
            phone_number = request.POST.get('phone_number')
            operator_code = request.POST.get('operator_code')
            tag = request.POST.get('tag')
            timezone = request.POST.get('timezone')

            client = Client(phone_number=phone_number,
                            operator_code=operator_code, tag=tag,
                            timezone=timezone)
            client.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'messages': 'A method doesn\'t avaible'})
