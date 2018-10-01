from rest_framework import serializers

from tweets.models import Tweet
from accounts.api.serializers import UserModelSerializer

class TweetModelSerializer(serializers.ModelSerializer):
	user = UserModelSerializer()
	
	class Meta:
		model = Tweet
		fields = [
			'user',
			'content'
		]
