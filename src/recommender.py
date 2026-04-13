import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """Represents a song and its attributes. Required by tests."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """Represents a user's taste preferences. Required by tests."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """OOP implementation of the recommendation logic."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns top k recommended songs based on OOP scoring."""
        scored_songs = []
        for song in self.songs:
            score = 0.0
            if song.genre == user.favorite_genre:
                score += 2.0
            if song.mood == user.favorite_mood:
                score += 1.0
            
            # Energy proximity calculation
            energy_diff = abs(song.energy - user.target_energy)
            score += max(0, 1.0 - energy_diff)
            
            scored_songs.append((score, song))
            
        # Sort descending by score
        scored_songs.sort(key=lambda x: x[0], reverse=True)
        return [song for score, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explains why a specific song was recommended to a user."""
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append("matches your favorite genre")
        if song.mood == user.favorite_mood:
            reasons.append("matches your current mood")
            
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.2:
            reasons.append("has the perfect energy level")
            
        if not reasons:
            return "This song might be an exciting new discovery!"
            
        return "This song " + " and ".join(reasons) + "."

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and casts numeric columns."""
    songs = []
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences with point logic."""
    score = 0.0
    reasons = []
    
    # 1. Genre matching (+2.0)
    if song['genre'] == user_prefs.get('genre'):
        score += 2.0
        reasons.append("Genre match (+2.0)")
        
    # 2. Mood matching (+1.0)
    if song['mood'] == user_prefs.get('mood'):
        score += 1.0
        reasons.append("Mood match (+1.0)")
        
    # 3. Energy similarity (Up to +1.0)
    if 'energy' in user_prefs:
        energy_diff = abs(song['energy'] - user_prefs['energy'])
        energy_score = max(0, 1.0 - energy_diff)
        score += energy_score
        reasons.append(f"Energy proximity (+{energy_score:.2f})")
        
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores and ranks all songs to return top k recommendations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))
        
    # Sort the list by the score index (1) in descending order
    scored_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return scored_songs[:k]