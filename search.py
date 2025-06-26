import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import requests
import re
import webbrowser

def search_google(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Try something more specific."
    except wikipedia.exceptions.PageError:
        return "No results found for your query."
    except requests.exceptions.ConnectionError:
        return "No internet connection."
    except Exception as e:
        return "No speakable output available"

def search_youtube(query):
    try:
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        response = requests.get(search_url)
        
        if response.status_code != 200:
            return "Failed to search YouTube."

        # Find video IDs using regex
        video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
        
        if not video_ids:
            return "Couldn't find any videos."

        top_video_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
        webbrowser.open(top_video_url)
        return f"Playing the top result for {query} on YouTube."
    
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred
    