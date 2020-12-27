from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from data.serializers import UmpireSerializers, TeamSerializers, \
    BatsmanSerializers, StackedSerializers
from data.models import Umpire, Deliveries, Matches
from django.db.models import Sum, Count
from django.views.decorators.csrf import csrf_exempt
from collections import defaultdict


def home(request):
    return render(request, 'home.html', {'data': 'cool'})


def prob1(request):
    return render(request, 'prob1.html', {'data': 'prob-1'})


def prob2(request):
    return render(request, 'prob2.html', {'data': 'prob-2'})


def prob3(request):
    return render(request, 'prob3.html', {'data': 'prob-3'})


def prob4(request):
    return render(request, 'prob4.html', {'data': 'prob-4'})


class Team(APIView):
    def get(self, request, format=None):
        data = Deliveries.objects.values('batting_team')\
            .annotate(dsum=Sum('total_runs')).order_by('dsum').reverse()

        serializer = TeamSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, form=None):
        year = request.data['year']
        top = int(request.data['top'])
        print(request.data)

        # SELECT batting_team, sum(total_runs) from Deliveries
        # where matches_id in (1,2,3,4,5,6,......) group by batting_team
        data = Deliveries.objects\
            .filter(match_id__in=Matches.objects.filter(season=year))\
            .values('batting_team').annotate(dsum=Sum('total_runs'))\
            .order_by('dsum').reverse()[:top]

        serializer = TeamSerializers(data, many=True)
        return Response(serializer.data)


class Batsman(APIView):
    def get(self, request, form=None):
        data = Deliveries.objects.values('batsman')\
            .annotate(runs=Sum('batsman_runs'))\
            .order_by('runs').reverse()[:10]

        serializer = BatsmanSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, form=None):
        year = request.data['year']
        top = int(request.data['top'])
        team = request.data['team']
        # team = "Royal Challengers Bangalore"
        print(request.data)

        if year == 'all' and team == 'all':
            data = Deliveries.objects.values('batsman')\
                .annotate(runs=Sum('batsman_runs'))\
                .order_by('runs').reverse()[:top]

        elif year == 'all' and team != 'all':
            data = Deliveries.objects.values('batsman')\
                .filter(batting_team=team)\
                .annotate(runs=Sum('batsman_runs'))\
                .order_by('runs').reverse()[:top]

        elif year != 'all' and team == 'all':
            id = [i.id for i in Matches.objects.filter(season=year).all()]
            data = Deliveries.objects.filter(match_id__in=id)\
                .values('batsman').annotate(runs=Sum('batsman_runs'))\
                .order_by('runs').reverse()[:top]

        else:
            id = [i.id for i in Matches.objects.filter(season=year).all()]
            data = Deliveries.objects.filter(match_id__in=id)\
                .values('batsman').annotate(runs=Sum('batsman_runs'))\
                .filter(batting_team=team).order_by('runs').reverse()[:top]

        serializer = BatsmanSerializers(data, many=True)
        return Response(serializer.data)


class Umpires(APIView):
    def get(self, request, form=None):
        umpire = Umpire.objects.values('nationality')\
            .annotate(total=Count('nationality'))
        serializer = UmpireSerializers(umpire, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        name = request.data['umpire']
        print(request.data)
        # name = ["New Zealand", "Australia"]
        data = Umpire.objects.values('nationality')\
            .filter(nationality__in=name).annotate(total=Count('nationality'))\
            .order_by('total').reverse()
        serializer = UmpireSerializers(data, many=True)
        return Response(serializer.data)


class Stacked(APIView):
    def get(self, request, form=None):

        year = [2017,2008, 2009]
        team = ["Chennai Super Kings"]
        team1 = Matches.objects.values('season', 'team1').filter(season__in=year, team1__in = team).annotate(total=Count('team1')).order_by('season','team1')
        team2 = Matches.objects.values('season', 'team2').filter(season__in=year, team2__in = team).annotate(total=Count('team2')).order_by('season','team2').values('total')

        for index, i in enumerate(team1):
            i['total'] = i['total'] + team2[index]['total']
        serializer = StackedSerializers(team1, many=True)
        return Response(serializer.data)

    def post(self, request, form=None):
        year = request.data['year']
        team = request.data['team']

        print(year)
        print(team)
        team1 = Matches.objects.values('season', 'team1').filter(season__in=year, team1__in = team).annotate(total=Count('team1')).order_by('season','team1')
        team2 = Matches.objects.values('season', 'team2').filter(season__in=year, team2__in = team).annotate(total=Count('team2')).order_by('season','team2').values('total')

        for index, i in enumerate(team1):
            i['total'] = i['total'] + team2[index]['total']
        serializer = StackedSerializers(team1, many=True)
        return Response(serializer.data)
