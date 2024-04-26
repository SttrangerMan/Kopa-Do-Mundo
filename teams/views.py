from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Team
from utils import (
    data_processing,
    ImpossibleTitlesError,
    InvalidYearCupError,
    NegativeTitlesError,
)


class TeamsView(APIView):
    def post(self, request):
        team_data = request.data

        try:
            data_processing(team_data)
        except (
            NegativeTitlesError,
            ImpossibleTitlesError,
            InvalidYearCupError,
        ) as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**team_data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request):
        teams = Team.objects.all()
        team_dict = []

        for team in teams:
            t = model_to_dict(team)
            team_dict.append(t)

        return Response(team_dict)
