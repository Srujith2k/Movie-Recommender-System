# Movie-Recommender-System

# Data: (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data)

Created Dataframes named movies and credits.
merged both the dataframes with title.
Selected important factors for review ['movie_id','title', 'overview', 'genres', 'keywords', 'cast', 'crew']
Checked if there is any null/missing data and dropped them using dropna function

# Preprocessing the Data:

making '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]' to ['Action', 'Adventure', 'Fantasy', 'Science Fiction']
Refined the data by making lists of each category and merging spaces.

# Vectorization

Finding similarities between the tags.
Here,
Did the vectorization for tags of each movie. (Text Vectorization)
Technique: Bag of words.{No stop words used}
from sklearn.feature_extraction.text import CountVectorizer

Applied Stemming on the vectors to remove similar kind of words. For example, {Love, Loving, loved} will be mapped to "love"
Calculated the cosine distance between each vector.
And for the recommendation the closest vector would be recommended.

# Creating the website:

Use Pycharm Community editor and create a new project using a virtual environment.
use pickle package to dump the movies_list and similarity list. and use it in the app.py:
pickle.dump(new_df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl','wb'))
to get movies.pkl and similarity.pkl mentioned in the website/app.py
Used streamlit for front-end.
To Run the app.py file.

# Open Terminal and enter the below command to launch the website in your local:

    streamlit run app.py
