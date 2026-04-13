"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.
"""

import os
from recommender import load_songs, recommend_songs


def main() -> None:
    # Ensure it finds the data path regardless of where the script is executed
    csv_path = "data/songs.csv"
    if not os.path.exists(csv_path):
        csv_path = "../data/songs.csv"

    songs = load_songs(csv_path) 
    print(f"🎵 Successfully loaded {len(songs)} songs from the catalog.\n")

    # Three diverse test profiles for evaluation
    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95}
    }

    for profile_name, user_prefs in profiles.items():
        print("="*60)
        print(f"👤 Testing Profile: {profile_name}")
        print(f"   Preferences: {user_prefs}")
        print("-" * 60)
        
        # Get top 3 recommendations
        recommendations = recommend_songs(user_prefs, songs, k=3)
        
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f" {i}. {song['title']} by {song['artist']}")
            print(f"    Tags : {song['genre'].capitalize()} | {song['mood'].capitalize()} | {song['energy']} Energy")
            print(f"    Score: {score:.2f}  =>  Because: {explanation}\n")


if __name__ == "__main__":
    main()
    