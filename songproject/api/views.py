from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from song_models.models import Song, SongUser
from .serializers import SongSerializer, SongUserSerializer
from .pagination import CustomPagination
from rest_framework import viewsets, permissions
from rest_framework import status

class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = CustomPagination
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def random(self, request):
        song = self.get_queryset().order_by('?').first()
        
        if song:
            serializer = self.get_serializer(song)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'detail': 'No songs available'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])
    def top(self, request):
        try:
            n = int(self.request.query_params.get('n', 3))
        except:
            return Response({'detail': 'Invalid parameter n'}, status=status.HTTP_400_BAD_REQUEST)
        
        top = self.get_queryset().order_by('-number_times_played')[:n]

        serializer = self.get_serializer(top, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search(self, request):
        text = self.request.query_params.get('title', None)
        songs = self.get_queryset()

        if not text:
            return Response({'detail': 'Missing title parameter'}, status=status.HTTP_400_BAD_REQUEST)

        song = songs.filter(title__icontains = text)

        if not song.exists():
            return Response({'detail': 'Song does not exists'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(song, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
class SongUserViewSet(viewsets.ModelViewSet):
    queryset = SongUser.objects.all()
    serializer_class = SongUserSerializer
    permission_classes = [permissions.IsAuthenticated]
