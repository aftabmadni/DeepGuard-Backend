#!/usr/bin/env bash
# build.sh

echo "Starting build process..."

# Install core dependencies first
pip install Django==5.0.6 gunicorn==21.2.0 whitenoise==6.6.0 django-cors-headers==4.3.1
pip install numpy==1.26.4 opencv-python==4.10.0.84 Pillow==10.3.0 requests==2.32.3

# Install torch with specific index for CPU
echo "Installing PyTorch..."
pip install torch==2.5.1+cpu torchvision==0.20.1+cpu --index-url https://download.pytorch.org/whl/cpu

# Try to install face-recognition dependencies separately (if needed)
# pip install dlib==19.24.0 --no-deps || echo "dlib installation failed, continuing..."
# pip install face-recognition==1.3.0 --no-deps || echo "face-recognition installation failed, continuing..."

# Collect static files
python manage.py collectstatic --noinput

echo "Build completed successfully!"