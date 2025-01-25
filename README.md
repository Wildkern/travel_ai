Personalized Travel Itinerary Generator

This project allows users to generate personalized travel itineraries using OpenAI's Gemini API. The application collects user preferences, including trip duration, destination, budget, and interests, and creates a detailed day-by-day travel itinerary.
Features

    Collect user inputs such as destination, budget, preferences, trip duration, and more.
    Generate personalized itineraries with recommendations for attractions, activities, accommodation, etc.
    Supports flexible input formats and provides relevant suggestions based on user preferences.
    Built using streamlit for the frontend, allowing users to interact with the application easily.

Requirements

Before running the application, ensure you have the following dependencies installed:

    Python 3.7+
    streamlit: For building the interactive interface.
    Python-dotenv: To securely load environment variables like the Gemini API key.

Install Dependencies

pip install -r requirements.txt

Sample requirements.txt

streamlit
google-generativeai
python-dotenv

Setup

    Clone this repository:

git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name

Create a .env file in the root directory and add your Gemini API key:

GEMINI_API_KEY=your_actual_api_key_here

Run the application:

    python app.py

    The Streamlit app will launch in your browser, allowing you to interact with the travel itinerary generator.

How It Works
User Interaction:

    The app asks the user for basic details such as the destination, trip duration, budget, and preferences (e.g., nature, adventure, etc.).
    Based on these inputs, the Gemini API generates personalized suggestions for activities, attractions, and accommodations.
    The app generates a day-by-day itinerary, which includes top-rated locations and hidden gems tailored to the user's interests.

Backend:

    The app uses the Google Gemini API to generate travel suggestions.
    It securely stores the API key using the dotenv library.

Example of Generated Itinerary
User Inputs:

    Destination: Paris
    Budget: Moderate
    Duration: 5 days
    Interests: Art, History, Local Cuisine

Generated Itinerary (Day-by-Day):

    Day 1: Arrival in Paris, check-in at a centrally located hotel, visit the Louvre Museum, dinner at a French bistro.
    Day 2: Morning visit to Notre-Dame Cathedral, afternoon at the Musée d'Orsay, dinner at a gourmet restaurant.
    Day 3: Day trip to Versailles Palace, explore the gardens, return to Paris for evening leisure.
    Day 4: Visit Montmartre, Sacré-Cœur, explore local cafes, and enjoy a cooking class.
    Day 5: Free day for shopping, farewell dinner with a Seine river cruise.



  # Screenshots 
  ![Screenshot from 2025-01-25 21-48-38](https://github.com/user-attachments/assets/a06f5d46-33d1-4f7c-a542-a3d302bdb942)


  ![Screenshot from 2025-01-25 21-48-44](https://github.com/user-attachments/assets/32418a2f-d075-42ef-859c-82fefb3a711d)




