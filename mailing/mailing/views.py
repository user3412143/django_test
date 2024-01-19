import os
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views import View

from .models import Client, Mailing

class MailDistribution(View):
    def send_mailing(request, mailing_id):
        try:
            mailing = Mailing.objects.get(id=mailing_id)
            clients = Client.objects.filter(
                    operator_code=mailing.client_filter_operator_code,
                    tag=mailing.client_filter_tag)
        except Mailing.DoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'A mailing id doesn\'t exist',
                                 'code': 0})
        except Client.DoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'A client doesn\t exist',
                                 'code': 0,})
        # send message
        for client in clients:
            # We send client.phone_number with mailing_id.message
            pass
        return JsonResponse({'status': 'success',
                             'code': 1})
    def cancel_mailing(request, mailing_id):
        mailing = get_object_or_404(Mailing, id=mailing_id)
        mailing.end_datetime = mailing.start_datetime
        mailing.save()
        return JsonResponse({'status': 'success',
                             'message': 'Send messages canceling',
                             'code': 1})


mail_obj = MailDistribution()
