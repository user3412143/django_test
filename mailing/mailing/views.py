from .models import Client, Mailing

from django.http import JsonResponse
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
            pass
        return JsonResponse({'status': 'success',
                             'message': 'Send messages canceling',
                             'code': 1})


mail_obj = MailDistribution()
