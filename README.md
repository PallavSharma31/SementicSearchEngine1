# Sementic-Search-Engine

This Django project, named Semantic Search Engine, is a powerful search engine designed specifically for e-commerce websites. It enables users to input their queries and retrieves the most relevant products from a database based on semantic similarity scores. By leveraging natural language processing techniques, the search engine aims to provide accurate and intuitive search results for enhanced user experience.

![intro_gif](https://github.com/pallav31sharma/Sementic-Search-Engine/assets/133598959/4e446073-f8a5-4a1c-8815-4efa0003ba08)



## Benefits of Semantic Search Engine

**"Semantic Search Engine" has real-life applications in various scenarios, especially in e-commerce websites. Here's an explanation of its real-life usage and how it differs from normal search:**

1.Enhanced Product Search Experience: The Semantic Search Engine improves the search experience for users on e-commerce websites. Instead of relying solely on keyword matching, it considers the semantic similarity between user queries and product descriptions. This means that users can search using natural language queries and still receive accurate and relevant product recommendations.

2.Improved Product Discovery: By utilizing semantic similarity, the search engine can identify products that closely match the user's intent, even if they don't explicitly use the exact search terms. This helps users discover relevant products that they may not have found through traditional keyword-based searches.

3.Higher Precision and Relevance: The Semantic Search Engine provides more precise and relevant search results compared to traditional search engines. It takes into account the meaning and context of user queries and product descriptions, enabling it to deliver more accurate recommendations that align with user intent.

4.Natural Language Support: The search engine understands and processes natural language queries effectively. Users can express their search queries in a more conversational and intuitive manner, similar to how they would ask a question or describe a product in a normal conversation. This makes the search process more user-friendly and accessible.

5.Contextual Understanding: The Semantic Search Engine goes beyond individual keywords and takes into account the context and meaning of the entire query. It understands the relationship between words and phrases, enabling it to provide more contextually relevant search results. This context-awareness helps in filtering out irrelevant products and improving the overall search quality.


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

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
```

## Usage

1. Start the Django development server.

   ```shell
   python manage.py runserver

2. Access the project through your web browser by visiting http://localhost:8000

3. Signup or login in case if you have an account already.
   
   <img width="948" alt="signup" src="https://github.com/pallav31sharma/Sementic-Search-Engine/assets/133598959/acb6bafe-eec3-4d75-a6ae-48311b2c0628">

   
   <img width="947" alt="login" src="https://github.com/pallav31sharma/Sementic-Search-Engine/assets/133598959/61d40c31-ac42-4e82-9811-c9f57f67128e">

4. Enter your search query in the provided search input field. Click the search button or press Enter to initiate the search.

   
   <img width="947" alt="search_page" src="https://github.com/pallav31sharma/Sementic-Search-Engine/assets/133598959/61c26b38-948f-4df0-a6ae-0b91e1e8eb33">

5. The search engine will compare your query with the product descriptions in the database and display the most relevant products based on semantic similarity scores. Browse the search results and click on individual products for more details.

 

   <img width="949" alt="product_page" src="https://github.com/pallav31sharma/Sementic-Search-Engine/assets/133598959/b479cee6-48e8-445f-896f-74de4738bd2c">


