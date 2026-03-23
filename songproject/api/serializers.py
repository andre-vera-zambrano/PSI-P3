from song_models.models import Song, SongUser
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    
class SongUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongUser
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        logged_user = self.context['request'].user
        validated_data['user'] = logged_user
        
        return super().create(validated_data)
    