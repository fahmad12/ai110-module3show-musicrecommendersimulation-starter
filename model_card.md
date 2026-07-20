# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Song Match 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

    Song Match 1.0 is a simulator that outputs musical recommendations based on the user's preferred genre, mood, and energy level. This is a classroom exploration, not yet something for real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

    The model provides each song with points based on how well the genre, mood, and energy levels match. The greater the match, the higher the points. Then, it outputs a list of songs, ranked by how high their scores are.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

    The catalog has 15 songs. Pop, jazz, lofi, classical, and country songs are represented, as well as happy and peaceful moods. I added in 5 songs (numbers 11-15) to the orignal dataset. Yes, there are still parts of musical taste missing in the dataset because as of now, it is too small.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

    My system works well for those whose whose preferred genres or energy levels are most common in the dataset.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

    The system behaves unfairly because it favors those profiles in which the genres matches the most common genres in the catalog. The most points are given for genre, so if a person perfers a specific genre and more songs of that genre are available, then they will get more points. This is a bias as it gives more points simply because of how many songs of a genre are in the catalog.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

The user profiles I tested are listed below:
I was surprised at how important energy was, when genre and mood didn't match or isn't mentioned. The simulator decides to go based off the energy then to find a song.

Terminal Output for Each Profile's Recommendations

```
==================================================
  TOP RECOMMENDATIONS
  For: genre=classical, mood=sad, energy=0.9
==================================================

1. Moonlit Sonata Redux — Elena Vasquez
   Score: 2.40
   Reasons: genre match (classical) (+2.0), energy closeness (0.30) (+0.40)

2. Storm Runner — Voltline
   Score: 0.99
   Reasons: energy closeness (0.91) (+0.99)

3. Gym Hero — Max Pulse
   Score: 0.97
   Reasons: energy closeness (0.93) (+0.97)

4. Sunrise City — Neon Echo
   Score: 0.92
   Reasons: energy closeness (0.82) (+0.92)

5. Concrete Dreams — MC Vertex
   Score: 0.90
   Reasons: energy closeness (0.80) (+0.90)
```

```
==================================================
  TOP RECOMMENDATIONS
  For: genre=kpop, mood=euphoric, energy=0.5
==================================================

1. Island Time — Palm Riddim
   Score: 1.00
   Reasons: energy closeness (0.50) (+1.00)

2. Golden Hour Blues — Ruby Lane
   Score: 0.95
   Reasons: energy closeness (0.45) (+0.95)

3. Desert Highway — Cactus Road
   Score: 0.95
   Reasons: energy closeness (0.55) (+0.95)

4. Midnight Coding — LoRoom
   Score: 0.92
   Reasons: energy closeness (0.42) (+0.92)

5. Focus Flow — LoRoom
   Score: 0.90
   Reasons: energy closeness (0.40) (+0.90)
```

```
==================================================
  TOP RECOMMENDATIONS
  For: genre=pop, mood=happy, energy=2.0
==================================================

1. Sunrise City — Neon Echo
   Score: 3.32
   Reasons: genre match (pop) (+2.0), mood match (happy) (+1.5), energy closeness (0.82) (+-0.18)

2. Gym Hero — Max Pulse
   Score: 1.93
   Reasons: genre match (pop) (+2.0), energy closeness (0.93) (+-0.07)

3. Rooftop Lights — Indigo Parade
   Score: 1.26
   Reasons: mood match (happy) (+1.5), energy closeness (0.76) (+-0.24)

4. Storm Runner — Voltline
   Score: -0.09
   Reasons: energy closeness (0.91) (+-0.09)

5. Concrete Dreams — MC Vertex
   Score: -0.20
   Reasons: energy closeness (0.80) (+-0.20)
```

```
==================================================
  TOP RECOMMENDATIONS
  For: genre=Pop, mood=Happy, energy=0.8
==================================================

1. Concrete Dreams — MC Vertex
   Score: 1.00
   Reasons: energy closeness (0.80) (+1.00)

2. Sunrise City — Neon Echo
   Score: 0.98
   Reasons: energy closeness (0.82) (+0.98)

3. Rooftop Lights — Indigo Parade
   Score: 0.96
   Reasons: energy closeness (0.76) (+0.96)

4. Night Drive Loop — Neon Echo
   Score: 0.95
   Reasons: energy closeness (0.75) (+0.95)

5. Storm Runner — Voltline
   Score: 0.89
   Reasons: energy closeness (0.91) (+0.89)
```

```
==================================================
  TOP RECOMMENDATIONS
  For: genre=None, mood=None, energy=None
==================================================

1. Sunrise City — Neon Echo
   Score: 0.00
   Reasons: no matching features

2. Midnight Coding — LoRoom
   Score: 0.00
   Reasons: no matching features

3. Storm Runner — Voltline
   Score: 0.00
   Reasons: no matching features

4. Library Rain — Paper Lanterns
   Score: 0.00
   Reasons: no matching features

5. Gym Hero — Max Pulse
   Score: 0.00
   Reasons: no matching features
```

Profile 1 vs 2: The classical profile puts Moonlit Sonata Redux first because it is a match; the kpop profile cnan't find a match, so its output is songs with some energy.

Profile 3 vs 4: Profile 3 (lowercase p in pop) has actual pop songs; profile 4 (uppercase p in Pop) ignores the genre and goes based off the energy.

Profile 4 vs 5: profiles either rank the songs by energy levels or don't rank them at all.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

    I would improve the model next by adding in more songs of diverse genres and energy levels so that the simulator can have a greater dataset to work with. 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

    I learned that it doesn't really matter if the recommender system completely understands a song or what it's about as long as the genre/mood/energy levels match what a person is looking for. This has changed the way I think about music recommendation apps because it has helped me realize that recommendations are based on matching choices, and that there is also some bias present depending on how many songs of a genre or mood are available.