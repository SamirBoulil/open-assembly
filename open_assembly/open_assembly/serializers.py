# coding: utf-8

from rest_framework import serializers

from .models import Circonscription
from .models import Deputy
from .models import Group
from .models import Mandate
from .models import Poll
from .models import Vote


class CirconscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Circonscription
        exclude = ('id', 'num_circo')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class DeputySerializer(serializers.ModelSerializer):
    group_id = serializers.ReadOnlyField(source='group.id')
    group_name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Deputy


class VoteSerializer(serializers.ModelSerializer):
    deputy_id = serializers.SerializerMethodField('get_deputy_serializer')

    def get_deputy_serializer(self, vote):
        return Deputy.objects.filter(mandates__votes__id=vote.id)[0].id

    class Meta:
        model = Vote


class PollForDepartmentSerializer(serializers.ModelSerializer):
    department_vote_count_ok = serializers.SerializerMethodField('get_votes_for_poll_and_department_no')
    department_vote_count_no = serializers.SerializerMethodField('get_votes_for_poll_and_department_yes')
    department_vote_count_abs = serializers.SerializerMethodField('get_votes_for_poll_and_department_abs')
    department_vote_count_not_voting = serializers.SerializerMethodField('get_votes_for_poll_and_department_not_voting')

    def get_votes_for_poll_and_department(self, poll, value):
        num_department = self.context['view'].kwargs['num_department']
        return Vote.objects\
            .filter(poll_id=poll.id)\
            .filter(mandate__circonscription__num_department=num_department)\
            .filter(decision=value)\
            .count()

    def get_votes_for_poll_and_department_no(self, poll):
        return self.get_votes_for_poll_and_department(poll, 0)

    def get_votes_for_poll_and_department_yes(self, poll):
        return self.get_votes_for_poll_and_department(poll, 1)

    def get_votes_for_poll_and_department_abs(self, poll):
        return self.get_votes_for_poll_and_department(poll, 2)

    def get_votes_for_poll_and_department_not_voting(self, poll):
        return self.get_votes_for_poll_and_department(poll, 3)

    class Meta:
        model = Poll


###################################################
# GARBAGE
# class FilteredListSerializer(serializers.ListSerializer):
    # def to_representation(self, data):
        # data = data.filter(user=self.request.user, edition__hide=False)
        # return super(FilteredListSerializer, self).to_representation(data)

# class PollForDepartmentSerializer2(serializers.ModelSerializer):
#     deputies = serializers.SerializerMethodField('get_deputies_votes')

#     def get_deputies_votes(self, poll):
#         self.context['poll_id'] = poll.id
#         num_department = self.context['view'].kwargs['num_department']

#         deputies = Deputy.objects.filter(
#                 votes__mandate__circonscription__num_department=num_department,
#                 votes__poll_id=poll.id
#                 )

#         serializer = DeputySerializer(instance=deputies, many=True, context=self.context)

#         return serializer.data

#     def get_votes_for_department(self, poll):
#         num_department = self.context['view'].kwargs['num_department']
#         votes = Vote.objects.filter(mandate__circonscription__num_department=num_department,
#                 poll_id=poll.id)
#         serializer = VoteSerializer(instance=votes, many=True)
#         return serializer.data

#     class Meta:
#         model = Poll
