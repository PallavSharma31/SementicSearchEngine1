# Sementic-Search-Engine

This Django project, named Semantic Search Engine, is a powerful search engine designed specifically for e-commerce websites. It enables users to input their queries and retrieves the most relevant products from a database based on semantic similarity scores. By leveraging natural language processing techniques, the search engine aims to provide accurate and intuitive search results for enhanced user experience.

<img width="947" alt="search_page" src="https://github.com/pallav31sharma/Sementic-Search-Engine/assets/133598959/65503847-ec23-4108-8cf8-2379023a44f2">

## Installation

To set up the Semantic Search Engine project, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/semantic-search-engine.git
 2. Create a virtual environment.

    ```shell
    python -m venv venv

 3. Activate the virtual environment.

    ```shell
    source venv/bin/activate

 4. Install the required dependencies.

    ```shell
    pip install -r requirements.txt


## Description    
   
This project makes use of the Sentence Transformer Model to convert the names of all the products into embeddings, the user query is also converted into embeddings so that the similarity score can be found between the user query and all products in the database, then the top 20 product is found out from the database on the basis of highest similarity score with the query.
