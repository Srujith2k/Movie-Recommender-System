# Movie-Recommender-System

Data: (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data)

Created Dataframes named movies and credits.
merged both the dataframes with title.
Selected important factors for review ['movie_id','title', 'overview', 'genres', 'keywords', 'cast', 'crew']
Checked if there is any null/missing data and dropped them using dropna function

Preprocessing the Data:
making '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]' to ['Action', 'Adventure', 'Fantasy', 'Science Fiction']
Refined the data by making lists of each category and merging spaces.

Vectorization
