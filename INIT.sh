#!/bin/bash

# Check if Miniconda is installed
if ! command -v conda &> /dev/null; then
    # If Miniconda is not installed, download and install it
    echo "Miniconda is not installed. Installing Miniconda..."
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda
    rm miniconda.sh
    export PATH="$HOME/miniconda/bin:$PATH"
fi

# Create and activate the Conda environment
echo "Creating and activating the 'tupi-env' Conda environment..."
conda create -n tupi-env python=3.10
conda activate tupi-env

# Install Poetry inside the Conda environment
echo "Installing Poetry inside 'tupi-env'..."
conda install -c conda-forge poetry

# Run 'poetry install' inside the Conda environment
echo "Running 'poetry install' inside 'tupi-env'..."
poetry install

# Use Poetry to run Python command to download NLTK files for Portuguese stopwords
echo "Downloading NLTK files for Portuguese stopwords..."
poetry run python -m nltk.downloader stopwords

echo "Installation complete."
