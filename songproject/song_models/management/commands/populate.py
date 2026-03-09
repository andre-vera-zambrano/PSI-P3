
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from song_models.models import Song, SongUser
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Limpia la base de datos y la puebla con datos de prueba'

    def handle(self, *args, **kwargs): 

        self.stdout.write('Limpiando base de datos...')

        SongUser.objects.all().delete() 
        Song.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write('Creando usuarios y superusuario...')

        superuser = User.objects.create_superuser(username='alumnnodb', password='alumnodb')

        u1 = User.objects.create(username = 'pedro', password = '123') 
        u2 = User.objects.create(username = 'dani', password = '123') 

        self.stdout.write('Creando las canciones...')

        s1 = Song.objects.create(
            title="Super Trouper",
            artist="ABBA",
            language="EN",
            audio_file="ABBA - Super Trouper.mp3",
            lrc_file="ABBA - Super Trouper.lrc",
            background_image="ABBA - Super Trouper.jpg",
            category="POP",
            number_times_played=0
        )

        s2 = Song.objects.create(
            title="Here In The Real World",
            artist="Alan Jackson",
            language="EN",
            audio_file="Alan Jackson - Here In The Real World.mp3",
            lrc_file="Alan Jackson - Here In The Real World.lrc",
            background_image="Alan Jackson - Here In The Real World.jpg",
            category="COUNTRY",
            number_times_played=0
        )

        s3 = Song.objects.create(
            title="Don't Forget to Remember",
            artist="Beegees",
            language="EN",
            audio_file="Beegees - Don't Forget to Remember.mp3",
            lrc_file="Beegees - Don't Forget to Remember.lrc",
            background_image="Beegees - Dont Forget to Remember.jpg",
            category="POP",
            number_times_played=0
        )
        
        self.stdout.write('Creando conexiones cancion-usuario...')

        SongUser.objects.create(
            song=s1,
            user=u1,
            correct_guesses=15,
            wrong_guesses=2,
            played_at=timezone.now()
        )

        SongUser.objects.create(
            song=s1,
            user=u2,
            correct_guesses=6,
            wrong_guesses=7,
            played_at=timezone.now()
        )

        SongUser.objects.create(
            song=s2,
            user=u1,
            correct_guesses=20,
            wrong_guesses=0,
            played_at=timezone.now()
        )

        SongUser.objects.create(
            song=s3,
            user=u2,
            correct_guesses=8,
            wrong_guesses=5,
            played_at=timezone.now()
        )

        self.stdout.write('Base de datos poblada con exito...')