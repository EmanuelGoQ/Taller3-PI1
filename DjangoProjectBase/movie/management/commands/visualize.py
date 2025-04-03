import numpy as np
import random
import requests
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Visualize movie embeddings"

    def handle(self, *args, **kwargs):

        movies = Movie.objects.all()
        for movie in movies:
            embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
            print(movie.title, embedding_vector[:5])  # Muestra los primeros valores
        
        movies = list(Movie.objects.all())
        
        if not movies:
            self.stdout.write(self.style.ERROR("No hay películas en la base de datos"))
            return

        movie = random.choice(movies)
        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)

        self.stdout.write(self.style.SUCCESS(f"🎬 Película seleccionada: {movie.title}"))
        self.stdout.write(f"📊 Embeddings (primeros 5 valores): {embedding_vector[:5]}")