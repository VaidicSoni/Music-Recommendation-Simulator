# 🎧 Model Card: VibeFinder 1.0

## 1. Model Name

**VibeFinder 1.0** ---

## 2. Intended Use

This system is a simulated content-based recommender designed to suggest 3 to 5 songs from a small, curated catalog based on a user's taste profile. It is intended strictly for classroom exploration and educational purposes to demonstrate algorithmic scoring rules. It makes the assumption that users have rigid preferences for specific genres, moods, and energy levels.

## 3. How the Model Works

VibeFinder 1.0 acts as a point-based judge for music. When a user requests music, the system looks at three specific traits of every song: Genre, Mood, and Energy Level.

It assigns a score to every song based on these rules:

- If the song's genre perfectly matches the user's favorite genre, it gets a massive boost (2 points).
- If the song's mood matches the user's requested mood, it gets a smaller boost (1 point).
- Finally, it looks at the song's energy level (on a scale of 0 to 1). The closer the song's energy is to the user's preferred energy, the more points it gets (up to 1 full point).

It adds these points together and recommends the songs with the highest totals.

## 4. Data

The dataset (`data/songs.csv`) is an artificially generated catalog of 15 songs. It includes columns for tempo, valence, and acousticness, though our current model only utilizes genre, mood, and energy. The data was expanded from 10 to 15 songs to include missing genres like EDM, Folk, Metal, Classical, and Hip-Hop. Because the catalog is tiny, it entirely fails to represent global music, non-western genres, or nuanced sub-genres.

## 5. Strengths

The system works remarkably well for users whose tastes perfectly align with the majority of the dataset (e.g., users who love "Pop" and "Lofi"). The logic excels in transparency; because the math is simple, we can generate highly accurate explanations (e.g., "Because: Genre match, Mood match") so the user knows exactly *why* they are seeing a track.

## 6. Limitations and Bias

The biggest flaw in VibeFinder 1.0 is that it creates strict "Filter Bubbles". By heavily weighting the "Genre" variable (+2.0 points), the system is extremely biased toward keeping users confined to a single category of music. It ignores great tracks that might share a similar sonic profile or energy just because the string label for the genre doesn't match perfectly. Furthermore, the system completely ignores lyrics, language, and cultural context.

## 7. Evaluation

I evaluated the system using a CLI script that pushed three diverse profiles through the recommender: "High-Energy Pop", "Chill Lofi", and "Deep Intense Rock".

I looked closely at the resulting output to see if the top 3 tracks matched my intuition of what those users would want. The system behaved exactly as expected for Pop and Lofi. However, the system surprised me when it suggested an EDM song for the Rock profile as the #2 result. This happened because the dataset only has one Metal/Rock song, so the model had to fall back heavily on "Energy Level" to fill out the remaining recommendations!

## 8. Future Work

To improve this model, I would:

1. **Balance Diversity:** Introduce a penalty if the top 3 songs are all from the exact same artist, forcing the algorithm to surface diverse creators.
1. **Soft Genre Matching:** Instead of strict String matching (`"pop" == "pop"`), I'd group similar genres together, so an "Indie Pop" fan might still get highly scored "Synthwave" tracks.
1. **Use More Features:** Begin integrating `tempo_bpm` and `valence` to differentiate between a "fast happy" song and a "slow happy" song.

## 9. Personal Reflection

Building VibeFinder taught me that recommender systems aren't "magic"—they are just rapid calculators assigning points based on human-defined rules. It was fascinating to discover that the bias in an AI doesn't just come from the data; it comes directly from the developer who decides which variables (like genre over tempo) deserve the highest numerical weight. This fundamentally changes how I view apps like Spotify, as I now recognize that every playlist I see is the result of thousands of tiny weighting decisions prioritizing my engagement.