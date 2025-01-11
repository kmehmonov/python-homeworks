import requests
import random

from apikeys import tmdb_api

base_url = "https://api.themoviedb.org/3/"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {tmdb_api}"
}

def fetch_genres():
    """Fetch and return genres as a list."""
    params = {"language": "en"}
    url = base_url + "genre/movie/list"
    res = requests.get(url, headers=headers, params=params)
    res.raise_for_status()
    return res.json().get("genres", [])

def discover_movies_by_genre(genre_id):
    """Discover movies by genre."""
    params = {
        "include_adult": False,
        "page": 1,
        "sort_by": "popularity.desc",
        "with_genres": genre_id,
    }
    url = base_url + "discover/movie"
    res = requests.get(url, headers=headers, params=params)
    res.raise_for_status()
    return res.json().get("results", [])

def get_random_movies(movies):
    """Return up to 5 random movies."""
    return random.sample(movies, min(5, len(movies)))

# Main logic
def main():
    genres = fetch_genres()
    if not genres:
        print("Failed to fetch genres.")
        return

    while True:
        print("\n" + "-" * 20)
        print("Select a genre:")
        for genre in genres:
            print(f"{genre['name']} - {genre['id']}")

        try:
            genre_id = int(input("Enter genre ID (or 0 to exit): "))
            if genre_id == 0:
                print("Exiting...")
                break

            movies = discover_movies_by_genre(genre_id)
            if not movies:
                print("No movies found for this genre. Try another one.")
                continue

            random_movies = get_random_movies(movies)
            print("\nMovies:")
            for index, movie in enumerate(random_movies):
                print(f"\n{'-' * 5} {index + 1} {'-' * 5}")
                print(f"ID: {movie['id']}")
                print(f"Title: {movie['title']}")
                print(f"Average Vote: {movie['vote_average']}")
                print(f"Release Date: {movie['release_date']}")
        except ValueError:
            print("Invalid input. Please enter a valid genre ID.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
