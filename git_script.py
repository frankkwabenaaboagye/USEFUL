import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(result.stdout.decode('utf-8'))
    else:
        print(f"Error: {result.stderr.decode('utf-8')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python git_script.py <commit_message>")
        sys.exit(1)

    commit_message = sys.argv[1]

    # Git add
    print("Adding all changes...")
    run_command("git add .")

    # Git commit
    print(f"Committing with message: {commit_message}")
    run_command(f'git commit -m "{commit_message}"')

    # Git status
    print("Checking status...")
    run_command("git status")

    # Git push
    print("Pushing to the repository...")
    run_command("git push")

    print("Done.")
