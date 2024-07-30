from github import Github
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

token = os.getenv('GITHUB_TOKEN')
if not token:
    raise ValueError("No GitHub token found in environment variables")

g = Github(token)

def check_rate_limit():
    rate_limit = g.get_rate_limit().core
    print(f"Rate limit: {rate_limit.remaining}/{rate_limit.limit}, Resets at: {rate_limit.reset}")

def list_repo_contents(repo_name):
    try:
        repo = g.get_repo(repo_name)
        contents = repo.get_contents("")
        for content_file in contents:
            print(content_file.path)
    except Exception as e:
        print(f"Error listing repository contents: {e}")

def create_issue(repo_name, title, body):
    try:
        repo = g.get_repo(repo_name)
        repo.create_issue(title=title, body=body)
    except Exception as e:
        print(f"Error creating issue: {e}")

if __name__ == "__main__":
    repo_name = "AmirZandiehprojects/Security-tools-evaluation"
    
    print("Checking rate limit:")
    check_rate_limit()

    print("Listing repository contents:")
    list_repo_contents(repo_name)
    
    print("\nCreating a test issue:")
    create_issue(repo_name, "Test Issue", "This is a test issue created by PyGitHub")
    
    print("\nRe-checking rate limit:")
    check_rate_limit()