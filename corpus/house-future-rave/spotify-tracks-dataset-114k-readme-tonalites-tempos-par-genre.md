---
titre: "sai-chaitanya-reddy/spotify-tracks-dataset — README (114 000 titres, 114 genres, CC0) + tonalité/mode/tempo calculés pour les genres house, edm, techno, trance, progressive-house…"
source: https://raw.githubusercontent.com/sai-chaitanya-reddy/spotify-tracks-dataset/main/README.md (+ spotify-tracks-dataset-detailed.csv, 19,4 Mo, même dépôt)
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: théorie spécifique (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Dataset public [DOC] (licence CC0 ; miroir du dataset Kaggle « Spotify Tracks Dataset » de maharshipandya). Le README est copié intégralement ; l'annexe donne des statistiques calculées localement sur le CSV.

# README.md (texte intégral)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=1DB954&height=200&section=header&text=Spotify%20Tracks%20Dataset&fontSize=50&fontColor=ffffff&fontAlignY=38&desc=114K%20Songs%20%C2%B7%20114%20Genres%20%C2%B7%2020%20Audio%20Features&descAlignY=58&descSize=18" width="100%"/>

<br/>

[![Spotify](https://img.shields.io/badge/Spotify_Web_API-1DB954?style=for-the-badge&logo=spotify&logoColor=white)](https://developer.spotify.com)
[![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Kaggle](https://img.shields.io/badge/View_on_Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/saichaitanyareddyai)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey?style=for-the-badge)](https://creativecommons.org/publicdomain/zero/1.0/)

<br/>

![Tracks](https://img.shields.io/badge/Tracks-114%2C000-1DB954?style=flat-square)
![Genres](https://img.shields.io/badge/Genres-114-20BEFF?style=flat-square)
![Artists](https://img.shields.io/badge/Artists-31%2C437-orange?style=flat-square)
![Columns](https://img.shields.io/badge/Columns-20-purple?style=flat-square)
![Missing](https://img.shields.io/badge/Missing_Values-None-brightgreen?style=flat-square)

</div>

<br/>

---

## 📖 Table of Contents

- [📌 Overview](#-overview)
- [📊 Dataset Statistics](#-dataset-statistics)
- [🧬 Feature Descriptions](#-feature-descriptions)
- [🚀 Quick Start](#-quick-start)
- [🎯 Use Cases](#-use-cases)
- [📈 Key Insights](#-key-insights)
- [🗂️ Repository Structure](#️-repository-structure)
- [🙌 Acknowledgements](#-acknowledgements)
- [👤 Author](#-author)
- [📜 License](#-license)

---

## 📌 Overview

> **A comprehensive collection of 114,000 Spotify tracks enriched with audio features — ideal for music analysis, genre classification, and building recommendation systems.**

This dataset was collected via the **Spotify Web API** and spans **114 unique music genres** with **31,437 unique artists**. Each track includes a rich set of audio features computed by Spotify's internal audio analysis engine.

Whether you are a **beginner** exploring EDA for the first time or an **advanced practitioner** building production ML models — this dataset provides meaningful real-world signals with zero missing values.

<br/>

> 🔗 **Also available on Kaggle →** [View Dataset](https://www.kaggle.com/saichaitanyareddyai)

---

## 📊 Dataset Statistics

<div align="center">

| Property | Value |
|:---:|:---:|
| 📁 **File Format** | CSV |
| 🎵 **Total Tracks** | 114,000 |
| 🎸 **Unique Genres** | 114 |
| 🧑‍🎤 **Unique Artists** | 31,437 |
| 📋 **Total Columns** | 20 |
| ❌ **Missing Values** | 0 |
| 📏 **Avg Popularity** | 33.2 / 100 |
| ⏱️ **Avg Duration** | ~3.8 minutes |
| 🎹 **Avg Tempo** | 122 BPM |
| 🎼 **Major Key Tracks** | 63.8% |
| 💃 **Avg Danceability** | 0.567 |
| ⚡ **Avg Energy** | 0.641 |

</div>

---

## 🧬 Feature Descriptions

<details>
<summary><b>🔍 Click to expand full feature table</b></summary>

<br/>

| Column | Type | Range | Description |
|---|---|---|---|
| `track_id` | String | — | Unique Spotify URI identifier for the track |
| `artists` | String | — | Performing artist name(s) |
| `album_name` | String | — | Album the track belongs to |
| `track_name` | String | — | Title of the track |
| `popularity` | Integer | 0 – 100 | Spotify popularity score (higher = more popular) |
| `duration_ms` | Integer | 0 – 5.2M | Track duration in milliseconds |
| `explicit` | Boolean | True/False | Whether the track has explicit lyrics |
| `danceability` | Float | 0.0 – 1.0 | How suitable a track is for dancing |
| `energy` | Float | 0.0 – 1.0 | Perceptual measure of intensity and activity |
| `key` | Integer | 0 – 11 | Musical key (0=C, 1=C♯, 2=D … 11=B) |
| `loudness` | Float | -49.5 – 4.5 | Overall loudness in decibels (dB) |
| `mode` | Integer | 0 or 1 | Modality — 1 = Major, 0 = Minor |
| `speechiness` | Float | 0.0 – 1.0 | Presence of spoken words in the track |
| `acousticness` | Float | 0.0 – 1.0 | Confidence the track is acoustic |
| `instrumentalness` | Float | 0.0 – 1.0 | Predicts whether a track has no vocals |
| `liveness` | Float | 0.0 – 1.0 | Detects presence of a live audience |
| `valence` | Float | 0.0 – 1.0 | Musical positiveness conveyed by the track |
| `tempo` | Float | 0 – 243 | Estimated tempo in beats per minute (BPM) |
| `time_signature` | Integer | 0 – 5 | Estimated time signature of the track |
| `track_genre` | String | 114 classes | Genre label assigned to the track |

</details>

---

## 🚀 Quick Start

### Step 1 — Clone the repository
```bash
git clone https://github.com/saichaitanyareddyai/spotify-tracks-dataset.git
cd spotify-tracks-dataset
```

### Step 2 — Install dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Step 3 — Load and explore
```python
import pandas as pd

# Load dataset
df = pd.read_csv('spotify-tracks-dataset-clean.csv')

# Basic info
print(f"Shape      : {df.shape}")
print(f"Genres     : {df['track_genre'].nunique()}")
print(f"Artists    : {df['artists'].nunique()}")
print(f"Null values: {df.isnull().sum().sum()}")

# Preview
df.head()
```

### Step 4 — Quick EDA example
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 6)

# Top 10 genres by average popularity
top_genres = (df.groupby('track_genre')['popularity']
                .mean()
                .sort_values(ascending=False)
                .head(10))

top_genres.plot(kind='bar', color='#1DB954', edgecolor='white')
plt.title('Top 10 Genres by Average Popularity', fontsize=14, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Average Popularity Score', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_genres.png', dpi=150)
plt.show()
```

---

## 🎯 Use Cases

| # | Use Case | Difficulty | Key Techniques |
|---|---|:---:|---|
| 1 | 🔍 **Exploratory Data Analysis** | `Beginner` | pandas, seaborn, matplotlib |
| 2 | 🎸 **Genre Classification** | `Intermediate` | Random Forest, XGBoost, SVM |
| 3 | 📈 **Popularity Prediction** | `Intermediate` | Linear Regression, Gradient Boosting |
| 4 | 🎧 **Music Recommendation System** | `Advanced` | K-Means, Cosine Similarity, Collaborative Filtering |
| 5 | 🧪 **Feature Engineering Practice** | `Intermediate` | Encoding, Binning, Normalization |
| 6 | 🧠 **Deep Learning Classification** | `Advanced` | Neural Networks, Embeddings, PyTorch |
| 7 | 📊 **Audio Feature Correlation Study** | `Beginner` | Heatmaps, Pairplots, Correlation Matrix |
| 8 | 🌍 **Genre Clustering** | `Intermediate` | DBSCAN, t-SNE, UMAP |

---

## 📈 Key Insights
```
╔══════════════════════════════════════════════════════════╗
║           DATASET HIGHLIGHTS AT A GLANCE                 ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  🎵  Avg Popularity    →   33.2 / 100  (mostly niche)    ║
║  ⚡  Avg Energy        →   0.641       (leans energetic)  ║
║  💃  Avg Danceability  →   0.567       (moderately dance) ║
║  😊  Avg Valence       →   0.474       (slightly sad)     ║
║  🎹  Avg Tempo         →   122 BPM     (pop/dance range)  ║
║  🎼  Major Key Tracks  →   63.8%       (majority upbeat)  ║
║  🎤  Avg Speechiness   →   0.085       (mostly musical)   ║
║  🎸  Avg Acousticness  →   0.315       (mix of both)      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```
## 🙌 Acknowledgements

- Data collected via the **[Spotify Web API](https://developer.spotify.com/documentation/web-api)**
- Audio features computed by Spotify's proprietary audio analysis pipeline
- Published for **educational and research purposes** under CC0 license
- Inspired by the global data science community on Kaggle

---

## 👤 Author

<div align="center">

**Sai Chaitanya Reddy**

*AI & Data Science Undergraduate*
*Vasireddy Venkatadri International Technological University (VVIT)*
*Hyderabad, Telangana, India*

<br/>

[![Kaggle](https://img.shields.io/badge/Kaggle-Follow_Me-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/saichaitanyareddyai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/saichaitanyareddyai)

</div>

---

## 📜 License

This dataset is released under the **[CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/)** license.

You are free to **copy, modify, distribute and use** this data — even for commercial purposes — without asking permission.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=1DB954&height=100&section=footer" width="100%"/>

**⭐ If this dataset helped your project, please star this repo — it helps others find it too!**

</div>


# Annexe (calcul local, mode synthese) : tonalité, mode et tempo par genre électronique (1000 titres par étiquette, champs Spotify `key`, `mode`, `tempo`)

Attention : `key`/`mode` sont des estimations automatiques de Spotify (mode majeur souvent attribué à la relative majeure d'un morceau mineur, et vice-versa) ; `tempo` est parfois divisé ou doublé (half-time). Lire ces chiffres comme des ordres de grandeur.

| Genre (étiquette Spotify) | n | mineur | tempo médian | Q1–Q3 | part 120–132 BPM | tonalités les plus fréquentes | toniques |
|---|---|---|---|---|---|---|---|
| edm | 1000 | 48 % | 123 | 105–128 | 45 % | B min 8 %, G#/Ab maj 7 %, G maj 7 %, F min 7 %, D maj 6 % | B 12 %, G 12 %, G#/Ab 11 %, C#/Db 11 % |
| house | 1000 | 49 % | 123 | 109–126 | 50 % | B min 8 %, G maj 8 %, C#/Db min 7 %, F#/Gb maj 7 %, C maj 6 % | C#/Db 12 %, F#/Gb 11 %, G 11 %, C 11 % |
| deep-house | 1000 | 54 % | 123 | 118–125 | 65 % | B min 7 %, G maj 7 %, F min 6 %, C#/Db min 6 %, C#/Db maj 6 % | C#/Db 11 %, C 11 %, B 10 %, G 10 % |
| chicago-house | 1000 | 50 % | 124 | 121–126 | 74 % | A#/Bb min 11 %, C#/Db maj 11 %, G maj 9 %, B min 9 %, C maj 7 % | C#/Db 15 %, B 13 %, A#/Bb 11 %, G 11 % |
| progressive-house | 1000 | 52 % | 126 | 122–128 | 70 % | F min 7 %, C#/Db maj 7 %, C maj 6 %, F#/Gb min 6 %, B min 6 % | C#/Db 12 %, F 12 %, B 10 %, F#/Gb 10 % |
| techno | 1000 | 44 % | 125 | 122–132 | 59 % | G maj 11 %, D maj 7 %, C#/Db maj 7 %, C maj 7 %, B min 6 % | G 13 %, C#/Db 12 %, B 9 %, C 9 % |
| minimal-techno | 1000 | 47 % | 125 | 122–127 | 77 % | G maj 12 %, C#/Db maj 9 %, D maj 7 %, B min 7 %, A#/Bb min 6 % | G 14 %, C#/Db 14 %, B 10 %, C 9 % |
| detroit-techno | 1000 | 50 % | 126 | 122–131 | 64 % | C#/Db maj 14 %, A#/Bb min 12 %, G maj 8 %, B min 7 %, E min 6 % | C#/Db 17 %, A#/Bb 13 %, B 12 %, F#/Gb 11 % |
| trance | 1000 | 52 % | 135 | 125–140 | 36 % | G maj 11 %, C#/Db maj 9 %, F#/Gb min 7 %, B min 7 %, A#/Bb min 7 % | G 16 %, C#/Db 13 %, F#/Gb 10 %, B 9 % |
| electro | 1000 | 43 % | 121 | 100–130 | 31 % | D maj 9 %, G#/Ab maj 8 %, C maj 7 %, G maj 6 %, B min 6 % | G#/Ab 12 %, D 10 %, C 10 %, F 10 % |
| club | 1000 | 34 % | 120 | 105–139 | 21 % | D maj 11 %, C#/Db maj 11 %, G maj 9 %, C maj 7 %, G#/Ab maj 6 % | C#/Db 14 %, D 12 %, G 12 %, C 9 % |
| dance | 1000 | 47 % | 120 | 101–130 | 26 % | D maj 7 %, G maj 7 %, C#/Db min 7 %, G#/Ab maj 7 %, C#/Db maj 7 % | C#/Db 13 %, G 11 %, B 10 %, A 10 % |
| dubstep | 1000 | 40 % | 140 | 115–150 | 14 % | C#/Db maj 11 %, D maj 9 %, B maj 6 %, G#/Ab maj 5 %, A maj 5 % | C#/Db 14 %, D 11 %, B 10 %, G 9 % |
| drum-and-bass | 1000 | 53 % | 174 | 140–174 | 6 % | C#/Db maj 12 %, A#/Bb min 9 %, F min 8 %, C maj 7 %, G maj 7 % | C#/Db 16 %, F 10 %, G 10 %, A#/Bb 10 % |
| hardstyle | 1000 | 53 % | 150 | 150–155 | 3 % | B min 8 %, C#/Db maj 8 %, G maj 8 %, F#/Gb min 7 %, C maj 6 % | G 11 %, C#/Db 11 %, C 10 %, F#/Gb 10 % |
| electronic | 1000 | 49 % | 123 | 105–137 | 30 % | C#/Db maj 8 %, D maj 7 %, F min 6 %, G#/Ab maj 6 %, B min 6 % | C#/Db 13 %, D 10 %, A 10 %, F 10 % |
| breakbeat | 1000 | 41 % | 130 | 120–142 | 31 % | C#/Db maj 13 %, G maj 13 %, A#/Bb min 9 %, B min 8 %, C maj 7 % | C#/Db 16 %, G 14 %, B 11 %, A#/Bb 10 % |
| garage | 1000 | 32 % | 126 | 105–146 | 19 % | D maj 11 %, C maj 10 %, A maj 10 %, G maj 8 %, B min 6 % | A 15 %, D 12 %, C 12 %, B 11 % |
| disco | 1000 | 37 % | 124 | 111–132 | 37 % | C maj 12 %, G maj 8 %, F maj 7 %, D maj 6 %, C#/Db maj 6 % | C 15 %, F 12 %, G 12 %, A 9 % |
| party | 1000 | 24 % | 132 | 126–140 | 38 % | C maj 15 %, G maj 10 %, F maj 8 %, G#/Ab maj 7 %, A maj 7 % | C 17 %, G 14 %, F 10 %, A 10 % |


## Complément : towenwolf/genre-classification `edm_songs.csv` (21 000 titres de playlists Spotify, 3000 par genre : techhouse, techno, trance, psytrance, trap, dnb, hardstyle) — https://raw.githubusercontent.com/towenwolf/genre-classification/master/edm_songs.csv

| Genre | n | mineur | tempo médian | Q1–Q3 | part 120–132 | tonalités | toniques |
|---|---|---|---|---|---|---|---|
| dnb | 3000 | 55 % | 174 | 174–174 | 0 % | C#/Db maj 11 %, A#/Bb min 10 %, F min 8 %, B min 6 %, C maj 6 % | C#/Db 15 %, F 11 %, A#/Bb 11 %, G#/Ab 10 % |
| hardstyle | 3000 | 64 % | 150 | 150–150 | 0 % | F min 9 %, A min 9 %, B min 8 %, C#/Db maj 7 %, A#/Bb min 6 % | C#/Db 13 %, F 12 %, A 12 %, B 9 % |
| psytrance | 3000 | 40 % | 143 | 140–145 | 1 % | G maj 20 %, B min 11 %, F#/Gb min 11 %, C#/Db maj 11 %, C maj 6 % | G 20 %, B 14 %, F#/Gb 14 %, C#/Db 14 % |
| techhouse | 3000 | 43 % | 125 | 124–126 | 99 % | C#/Db maj 11 %, B min 10 %, G maj 9 %, C maj 7 %, A#/Bb min 6 % | B 15 %, C#/Db 15 %, G 11 %, F#/Gb 10 % |
| techno | 3000 | 42 % | 128 | 126–131 | 80 % | G maj 18 %, C#/Db maj 12 %, B min 10 %, A#/Bb min 7 %, D maj 7 % | G 19 %, C#/Db 18 %, B 13 %, F#/Gb 10 % |
| trance | 3000 | 56 % | 136 | 130–138 | 33 % | C#/Db maj 8 %, F#/Gb min 7 %, G maj 7 %, A min 6 %, F min 6 % | C#/Db 12 %, F#/Gb 12 %, G 11 %, C 10 % |
| trap | 3000 | 40 % | 150 | 145–150 | 0 % | C#/Db maj 23 %, D maj 7 %, B min 7 %, F min 7 %, A maj 6 % | C#/Db 27 %, B 12 %, D 8 %, F 8 % |
