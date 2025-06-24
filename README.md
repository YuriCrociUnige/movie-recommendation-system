## 📘 Project Overview: Movie Recommendation System 📘

This project explores graph based recommendation models using the [MovieLens 20M dataset](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset). Starting from a classic item based KNN as a baseline, it progressively introduces more advanced models such as LightGCN and Graph Convolutional Networks to improve movie recommendations through graph representation learning.

🎯 The goal is to leverage all available information in the dataset, including user ratings, movie genres, tag relevance scores, and user–movie interaction structure, to build more accurate and personalized recommendations.

⚙️ The preprocessing phase is handled using SQL queries in DuckDB for efficient filtering over the large relational dataset, followed by data transformation and preparation in Pandas.

💻 Modeling is implemented with PyTorch for graph based architectures, while the simple KNN baseline is built using the scikit-learn library.

📊 Each step of the project is available and documented through Jupyter notebooks and a structured Python pipeline, providing clear justifications, transparency, and evaluation results for the audience.


