import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
# Configure the Gemini API with your API key
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define system and user prompts for creating the itinerary
def get_system_prompt():
    return """You are an expert travel planner. Your task is to create personalized travel itineraries based on user preferences. 
    Follow these guidelines:
    1. Extract and consider all relevant user preferences
    2. Create detailed day-by-day itineraries
    3. Include specific timing for activities
    4. Consider budget constraints
    5. Account for travel time between locations
    6. Suggest local restaurants matching dietary preferences
    7. Include practical tips and recommendations"""

def get_refined_preferences(basic_info):
    refinement_prompt = f"""Based on this basic information: {basic_info}
    Please ask for clarification on:
    1. Dietary preferences or restrictions
    2. Specific interests or activities they enjoy
    3. Walking/mobility preferences
    4. Accommodation preferences
    5. Any other crucial details needed for planning
    
    Format the response as clear, individual questions."""
    
    response = model.generate_content(refinement_prompt)
    return response.text

def generate_itinerary(all_preferences):
    itinerary_prompt = f"""Create a detailed travel itinerary based on these preferences: {all_preferences}
    
    Please include:
    1. Day-by-day breakdown
    2. Specific timing for each activity
    3. Restaurant recommendations
    4. Transportation suggestions
    5. Estimated costs
    6. Local tips and tricks
    
    Format the response in a clear, organized manner with proper headings and bullet points."""
    
    response = model.generate_content(itinerary_prompt)
    return response.text

# Streamlit interface
def app():
    st.title("🌍 AI Travel Planner")
    st.markdown("Let's create your personalized travel itinerary!")
    
    # Input Section for Travel Preferences
    destination = st.text_input("Where would you like to go?")
    duration = st.number_input("How many days is your trip?", min_value=1, max_value=30, value=5)
    budget = st.selectbox("What's your budget level?", options=["Budget", "Moderate", "Luxury"])
    purpose = st.text_input("What's the main purpose of your trip? (e.g., relaxation, adventure, culture)")
    additional_info = st.text_area("Any additional preferences or details?")
    
    if st.button("Generate Itinerary"):
        basic_info = f"Destination: {destination}, Duration: {duration} days, Budget: {budget}, Purpose: {purpose}"
        
        # Get refined preferences from the Gemini model
        refined_preferences = get_refined_preferences(basic_info)
        
        # Merge basic and additional preferences for generating the final itinerary
        all_preferences = f"{basic_info}\nAdditional Preferences: {additional_info}"
        
        # Generate itinerary using Gemini API
        itinerary = generate_itinerary(all_preferences)
        
        # Display the itinerary
        st.subheader("Your Personalized Itinerary")
        st.write(itinerary)

        # Allow the user to download the itinerary as a text file
        st.download_button(
            label="Download Itinerary",
            data=itinerary,
            file_name="travel_itinerary.txt",
            mime="text/plain"
        )

# Run the Streamlit app
if __name__ == "__main__":
    app()
