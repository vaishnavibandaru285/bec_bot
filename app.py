from flask import Flask, request, jsonify, redirect
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# URL of the website to scrape for information
WEBSITE_URL = "http://becbapatla.ac.in/"


def scrape_website(user_query):
    try:
        # Fetch the website content
        response = requests.get(WEBSITE_URL)
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find relevant information based on the user query
            if "about" in user_query:
                # Example: Extract admission-related information
                admission_info = soup.find("div", class_="about")
                # Example using CSS selectors
                about = soup.select("p:contains('about')")
                if about:
                    return admission_info[0].get_text(strip=True)

                else:
                    return "No admission information found on the website."
            elif "courses" in user_query:
                # Example: Extract information about courses
                courses_info = soup.find("div", class_="courses-info")
                if courses_info:
                    return courses_info.get_text(strip=True)
                else:
                    return "No courses information found on the website."
            elif "facilities" in user_query:
                # Example: Extract information about facilities
                facilities_info = soup.find("div", class_="facilities-info")
                if facilities_info:
                    return facilities_info.get_text(strip=True)
                else:
                    return "No facilities information found on the website."
            else:
                return "Sorry, I couldn't find relevant information for your query."
        else:
            return "Failed to fetch information from the website."
    except Exception as e:
        return f"Error: {e}"


@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    if request.method == 'GET':
        # Redirect GET requests to the website
        return redirect(WEBSITE_URL)
    elif request.method == 'POST':
        # Get user query from the Telegram bot request
        data = request.get_json()
        user_query = data['query']

        # Fetch information from the website based on the user query
        fetched_info = scrape_website(user_query)

        # Return the fetched information to the Telegram bot
        return jsonify({'response': fetched_info})


# Redirect root URL to get_info endpoint
@app.route('/')
def root():
    return redirect('/get_info')


if __name__ == '__main__':
    app.run(debug=True)
