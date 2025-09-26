# votes/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vote
from nominations.models import Nomination

class VoteSerializer(serializers.ModelSerializer):
    voter = serializers.ReadOnlyField(source='voter.username')
    candidate_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='candidate', write_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'voter', 'candidate_id', 'timestamp']
        read_only_fields = ['id', 'voter', 'timestamp']

    def validate(self, data):
        request = self.context.get('request')
        if request is None:
            raise serializers.ValidationError("Request context required.")
        voter = request.user
        candidate = data['candidate']

        # candidate must have an approved nomination
        if not Nomination.objects.filter(user=candidate, status='Approved').exists():
            raise serializers.ValidationError("Candidate is not approved for voting.")

        # categories (may be None)
        voter_cat = getattr(voter.profile.category, 'name', None)
        candidate_cat = getattr(candidate.profile.category, 'name', None)

        # voting rules
        if voter_cat in ('Service Provider', 'Designer'):
            raise serializers.ValidationError("Users in your category are not allowed to vote.")

        if voter_cat == 'Manufacturer' and candidate_cat not in ('Designer', 'Service Provider'):
            raise serializers.ValidationError("Manufacturers can vote only for Designers and Service Providers.")

        if voter_cat == 'Retailer' and candidate_cat == 'Retailer':
            raise serializers.ValidationError("Retailers cannot vote for other Retailers.")

        # prevent duplicate vote for same candidate by same voter
        if Vote.objects.filter(voter=voter, candidate=candidate).exists():
            raise serializers.ValidationError("You have already voted for this candidate.")

        return data

    def create(self, validated_data):
        request = self.context['request']
        return Vote.objects.create(voter=request.user, candidate=validated_data['candidate'])
