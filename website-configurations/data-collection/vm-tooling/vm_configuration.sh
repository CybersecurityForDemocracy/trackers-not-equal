sudo apt install -y python3.11-venv
# Check if google-chrome is installed
if ! command -v google-chrome &> /dev/null
then
    echo "Google Chrome is not installed. Installing..."
    # Download and install Google Chrome
    if [ -f .env ]; then
        export $(grep -v '^#' .env | xargs)
    fi
    gsutil cp $gs://{MY_BUCKET}/google-chrome-stable_current_amd64.deb .
    sudo apt-get update
    sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
    # Clean up downloaded .deb file
    rm google-chrome-stable_current_amd64.deb
fi

# python environment installation
sudo apt-get install -y python3.11-venv

# create new virtual environment
/usr/bin/env python3 -m venv myenv
# activate my python environment
source myenv/bin/activate

# install dependencies
pip install -r requirements.txt

# Update the package list
sudo apt-get update

# Install xvfb
sudo apt-get install -y xvfb

# install gnome-screenshot
sudo apt-get install -y gnome-screenshot

# start server for file uploads
# nohup python server.py > server_output.log 2>&1 &

# Check if Xvfb is already running
if ! pgrep -x "Xvfb" > /dev/null
then
    # Start Xvfb
    Xvfb :99 -screen 0 1024x768x16 &
    echo "Xvfb started."
else
    echo "Xvfb is already running."
fi

# set display environment variable
echo "Setting display variable"
export DISPLAY=:99
echo "$DISPLAY"

# run python script
echo "kicking off script"
python3 data_collection_script_linux.py