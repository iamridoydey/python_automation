import subprocess
import sys
import time

# Get the command argument
if len(sys.argv) < 2:
    print("Usage: python < this file name > < deployment name >")
    sys.exit(1)

# Deployment name
deployment_name = sys.argv[1]
    
# Function to check the deployment status
def isDeployed(deployment_name: str) -> bool:
    result = subprocess.run(
        ["kubectl", "get", f"deployment/{deployment_name}"],
        capture_output=True,
        text=True
    )
    
    return "1/1" in result.stdout


if __name__ == "__main__":
    while not isDeployed(deployment_name):
        print(f"Waiting for deployment/{deployment_name} to be deployed")
        # Sleep for 10 seconds
        time.sleep(10)
        
    print(f"deployment/{deployment_name} successfully deployed")