# coding: utf-8

from rest_framework import generics
from rest_framework import filters

from .models import Deputy
from .models import Poll
from .models import Circonscription 

from .models import Vote

from .serializers import DeputySerializer
from .serializers import CirconscriptionSerializer
from .serializers import VoteSerializer
from .serializers import PollForDepartmentSerializer


class CirconscriptionViewSet(generics.ListAPIView):
    serializer_class = CirconscriptionSerializer

    def get_queryset(self):
        return Circonscription.objects.all()


class DeputiesForDepartmentViewSet(generics.ListAPIView):
    query_set = Deputy.objects.all()
    serializer_class = DeputySerializer

    def get_queryset(self):
        num_department = self.kwargs['num_department']
        return Deputy.objects.filter(mandates__circonscription__num_department=num_department).distinct()


class PollsForDepartmentViewSet(generics.ListAPIView):
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 100
    serializer_class = PollForDepartmentSerializer

    def get_queryset(self):
        num_department = self.kwargs['num_department']
        return Poll.objects.filter(votes__mandate__circonscription__num_department=num_department).order_by('-poll_date')


class VotesForPollAndDepartmentViewSet(generics.ListAPIView):
    serializer_class = VoteSerializer

    def get_queryset(self):
        num_department = self.kwargs['num_department']
        poll_id = self.kwargs['poll_id']
        return Vote.objects.filter(poll_id=poll_id).filter(mandate__circonscription__num_department=num_department)


############################
# GARBAGE
# class FullPollsForDepartmentViewSet(generics.ListAPIView):
    # serializer_class = PollForDepartmentSerializer2

    # def get_queryset(self):
        # num_department = self.kwargs['num_department']
        # queryset = Poll.objects.filter(votes__mandate__circonscription__num_department=num_department).distinct().order_by('-poll_date')

        # return queryset


# class VotesForDeputyView(generics.ListAPIView):
    # serializer_class = DeputyDetailsSerializer

    # def get_queryset(self):
        # """ Retrieves the list of votes for one deputy and the
        # decree information.
        # """
        # deputy_slug = self.kwargs['deputy_slug']
        # queryset = Deputy.objects.filter(slug=deputy_slug)

        # is_solemn = self.request.query_params.get('is_solemn', None)
        # if is_solemn is not None:
            # queryset = queryset.filter(votes__poll__is_solemn=is_solemn)

        # return queryset
