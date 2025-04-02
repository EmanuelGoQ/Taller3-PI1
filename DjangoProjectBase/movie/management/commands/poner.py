import os
import requests
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Integrate images from a folder into the database"

    def handle(self, *args, **kwargs):

        # ✅ Fetch all movies
        movies = Movie.objects.all()
        self.stdout.write(f"Found {movies.count()} movies")

        updated_count = 0

        try:    
            movie = Movie.objects.get(title='Fairyland: A Kingdom of Fairies')
            image_filename = "m_Fairyland- A Kingdom of Fairies.png"
            image_relative_path = os.path.join('movie/images', image_filename)
            movie.image = image_relative_path
            movie.save()

            updated_count += 1

            movie = Movie.objects.get(title="The '?' Motorist")
            image_filename = "m_The motorist.jpg"
            image_relative_path = os.path.join('movie/images', image_filename)
            movie.image = image_relative_path
            movie.save()

            updated_count += 1

            movie = Movie.objects.get(title='The Inside of the White Slave Traffic')
            image_filename = "m_The Inside of the White Slave Traffic.jpg"
            image_relative_path = os.path.join('movie/images', image_filename)
            movie.image = image_relative_path
            movie.save()

            updated_count += 1

            movie = Movie.objects.get(title="The Avenging Conscience: or 'Thou Shalt Not Kill'")
            image_filename = "m_The Avenging Conscience or 'Thou Shalt Not Kill'.jpg"
            image_relative_path = os.path.join('movie/images', image_filename)
            movie.image = image_relative_path
            movie.save()

            updated_count += 1

        except Exception as e:
            self.stderr.write(f"Failed for {movie.title}: {e}")
            return
        
        self.stdout.write(self.style.SUCCESS(f"Process finished {updated_count} movies updated."))