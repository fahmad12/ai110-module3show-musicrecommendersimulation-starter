# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

  Done in "How the Model Works" section of model_card.md
---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

  In my version, the 'Recommender' computes a score for each song by adding 2 points if the genre matches, 1.5 points if the mood matches, and up to 1 point if the energy matches. The higher the total number of points, the better the song fits. You choose what songs to recommend based on which is higher on the ranked list. The specific features the 'Song' and 'UserProfile' will include are genre and mood, and favorite genre and favorite mood, respectively.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Loaded songs: 15

==================================================
  TOP RECOMMENDATIONS
  For: genre=pop, mood=happy, energy=0.8
==================================================

1. Sunrise City — Neon Echo
   Score: 4.48
   Reasons: genre match (pop) (+2.0), mood match (happy) (+1.5), energy closeness (0.82) (+0.98)

2. Gym Hero — Max Pulse
   Score: 2.87
   Reasons: genre match (pop) (+2.0), energy closeness (0.93) (+0.87)

3. Rooftop Lights — Indigo Parade
   Score: 2.46
   Reasons: mood match (happy) (+1.5), energy closeness (0.76) (+0.96)

4. Concrete Dreams — MC Vertex
   Score: 1.00
   Reasons: energy closeness (0.80) (+1.00)

5. Night Drive Loop — Neon Echo
   Score: 0.95
   Reasons: energy closeness (0.75) (+0.95)

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

  When the weight of the genre changed from 2.0 to 0.5, it gave more priority to the mood and recategorized based off that.

  By adding a valence, it ranked the songs with happier tones higher than those without.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

  - Small pool of songs (small sample size)
  - Results don't vary much

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

  Done in model_card.md

