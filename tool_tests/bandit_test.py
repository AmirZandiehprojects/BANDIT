import subprocess
import json

def run_bandit(file_path):
    result = subprocess.run(['bandit', '-f', 'json', '-r', file_path], capture_output=True, text=True)
    return json.loads(result.stdout)

if __name__ == "__main__":
    file_path = "sample_code/vulnerable_code.py"
    results = run_bandit(file_path)
    print(json.dumps(results, indent=2))

    # Count issues by severity
    issue_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
    for result in results['results']:
        issue_counts[result['issue_severity']] += 1

    print("\nIssue Summary:")
    for severity, count in issue_counts.items():
        print(f"{severity}: {count}")