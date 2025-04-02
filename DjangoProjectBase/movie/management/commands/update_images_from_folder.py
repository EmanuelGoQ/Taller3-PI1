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

        for movie in movies:
            try:
                image_filename = f"m_{movie.title}.png"
                # ✅ Call the helper function
                image_relative_path = os.path.join('movie/images', image_filename)
                
                image_path = os.path.join('media', image_relative_path)
                if not os.path.exists(image_path):
                    self.stderr.write(f"file '{image_path}' not found.")
                    continue

                # ✅ Update database
                movie.image = image_relative_path
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated image for: {movie.title}"))

            except Exception as e:
                self.stderr.write(f"Failed for {movie.title}: {e}")
                break

        self.stdout.write(self.style.SUCCESS(f"Process finished {updated_count} movies updated."))