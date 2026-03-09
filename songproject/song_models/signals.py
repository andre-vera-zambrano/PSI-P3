from django.db.models.signals import post_save
from django.dispatch import receiver
from song_models.models import SongUser

@receiver(post_save, sender=SongUser)
def update_song_play_count(sender, instance, created, **kwargs):
    if created:
        song = instance.song
        song.number_times_played += 1
        song.save()