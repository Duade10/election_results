from datetime import datetime

from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Party
from .models import PollingUnit, AnnouncedPuResults, Lga


def polling_unit_results(request):
    context = {}

    if request.method == 'POST':
        polling_unit_id = request.POST.get('polling_unit_id')

        if polling_unit_id == 'none':
            context['error'] = "Please enter a valid polling unit ID."
            return render(request, 'results/polling_unit_results.html', context)

        lgas = Lga.objects.filter(state_id=25)
        polling_units = PollingUnit.objects.filter(polling_unit_id=polling_unit_id,
                                                   lga_id__in=lgas.values_list('uniqueid', flat=True))

        if polling_units.exists():
            results = AnnouncedPuResults.objects.filter(
                polling_unit_uniqueid__in=polling_units.values_list('uniqueid', flat=True))

            context = {
                'polling_units': polling_units,
                'results': results
            }
        else:
            context['error'] = f"No polling unit found with ID {polling_unit_id} in Delta State."
    lgas = Lga.objects.filter(state_id=25)
    polling_unit_ids = PollingUnit.objects.filter(lga_id__in=lgas.values_list('uniqueid', flat=True)).values_list(
        'polling_unit_id', flat=True).distinct()
    context['polling_unit_ids'] = polling_unit_ids

    return render(request, 'results/polling_unit_results.html', context)


def lga_results(request):
    lgas = Lga.objects.filter(state_id=str(25))

    if request.method == 'POST':
        lga_id = request.POST.get('lga')
        lga = get_object_or_404(Lga, uniqueid=lga_id)
        polling_units = PollingUnit.objects.filter(lga_id=lga.lga_id)
        results = AnnouncedPuResults.objects.filter(
            polling_unit_uniqueid__in=polling_units.values_list('uniqueid', flat=True))
        summed_results = results.values('party_abbreviation').annotate(total_score=Sum('party_score'))
        context = {
            'lgas': lgas,
            'selected_lga': lga,
            'results': summed_results
        }
    else:
        context = {'lgas': lgas}

    return render(request, 'results/lga_results.html', context)


def new_polling_unit(request):
    if request.method == 'POST':

        polling_unit_id = request.POST.get('polling_unit_id')
        parties = Party.objects.all()

        for party in parties:
            score = request.POST.get(f'party_{party.partyid}')
            if score:
                AnnouncedPuResults.objects.create(
                    polling_unit_uniqueid=polling_unit_id,
                    party_abbreviation=party.partyid,
                    party_score=int(score),
                    entered_by_user=request.POST.get('entered_by_user'),
                    date_entered=datetime.now(),
                    user_ip_address=request.META.get('REMOTE_ADDR')
                )

        return render(request, 'results/success.html')
    else:
        parties = Party.objects.all()
        context = {'parties': parties}
        return render(request, 'results/new_polling_unit.html', context)
