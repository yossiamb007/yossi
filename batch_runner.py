import subprocess
import os


def run_batch_file(batch_file_name):
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the full path to the batch file
    batch_file_path = os.path.join(current_directory, batch_file_name)

    # Check if the batch file exists
    if not os.path.isfile(batch_file_path):
        print(f"Batch file '{batch_file_name}' not found in the current directory.")
        return

    try:
        # Run the batch file
        result = subprocess.run(batch_file_path, shell=True, check=True)
        print(f"Batch file '{batch_file_name}' executed successfully with return code {result.returncode}.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch file '{batch_file_name}': {e}")


if __name__ == "__main__":
    # Specify the name of the batch file to run
    batch_file_name = "auto_runner.bat"

    # Run the batch file
    run_batch_file(batch_file_name)
