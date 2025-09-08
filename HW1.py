import requests
import sys

BASE_URL = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

STUDENT_INFO = {
    "UCID": "rm942",   
    "first_name": "Rayhan",
    "last_name": "Mohammed",
    "github_username": "RayM2",
    "discord_username": "@raymoh1",  
    "favorite_cartoon": "Spongebob Squarepants",
    "favorite_language": "Python",
    "movie_or_game_or_book": "NBA 2K",
    "section": "101"
}


def post_student():
    try:
        resp = requests.post(BASE_URL, json=STUDENT_INFO, timeout=10)
        print("POST Status:", resp.status_code)
        print("Response:", resp.text)
        resp.raise_for_status()
    except requests.RequestException as e:
        print("POST failed:", e, file=sys.stderr)


if __name__ == "__main__":
    print("---- POST ----")
    post_student()
