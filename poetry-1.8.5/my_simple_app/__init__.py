"""
Simple Poetry example application.
Demonstrates using production dependencies (requests).
"""
import requests


def fetch_data(url):
    """Fetch data from URL using requests library (production dependency)."""
    response = requests.get(url)
    return response.json()


def main():
    """Main application entry point."""
    print("Fetching GitHub user data...")
    data = fetch_data("https://api.github.com/users/github")
    print(f"GitHub user: {data['name']}")
    print(f"Bio: {data['bio']}")
    print(f"Public repos: {data['public_repos']}")


if __name__ == "__main__":
    main()
