import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
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
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts, converting numeric columns to int/float."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for col in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
                row[col] = float(row[col])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user prefs (genre +2, mood +1.5, energy up to +1) and return (score, reasons)."""
    score = 0.0
    reasons: List[str] = []

    # Genre match: exact match earns the most points.
    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
        reasons.append(f"genre match ({song['genre']}) (+2.0)")

    # Mood match: exact match earns medium points.
    if song["mood"] == user_prefs.get("mood"):
        score += 1.5
        reasons.append(f"mood match ({song['mood']}) (+1.5)")

    # Energy closeness: reward songs whose energy is near the user's target.
    # Both values are on a 0-1 scale, so 1 - gap gives up to +1.0.
    if "energy" in user_prefs:
        gap = abs(song["energy"] - user_prefs["energy"])
        energy_points = 1.0 - gap
        score += energy_points
        reasons.append(f"energy closeness ({song['energy']:.2f}) (+{energy_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k as (song, score, explanation), ranked highest first."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no matching features"
        scored.append((song, score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
