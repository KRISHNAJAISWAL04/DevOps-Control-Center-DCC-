BOOTSTRAP_COMMAND = """
sudo apt update &&
sudo apt install -y docker.io git &&
sudo systemctl enable docker &&
sudo systemctl start docker &&
docker --version &&
git --version
"""