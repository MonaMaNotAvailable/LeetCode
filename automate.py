import subprocess
import sys

def git_add_commit_push(commit_message):
    try:

	# Git status
        subprocess.run(["git", "status"])

        # Git add
        subprocess.run(["git", "add", "."])

        # Git commit
        subprocess.run(["git", "commit", "-m", commit_message])

        # Git push
        subprocess.run(["git", "push", "origin", "main"])

        print("Changes successfully added, committed, and pushed: ", commit_message)

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 automate.py 'commit message(if space exists)'")
        sys.exit(1)

    commit_message = sys.argv[1]
    git_add_commit_push(commit_message)

if __name__ == "__main__":
    main()