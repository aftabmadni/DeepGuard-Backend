#!/usr/bin/env bash
set -o errexit

echo "Installing light dependencies first..."
pip install Django==5.0.6 gunicorn==21.2.0 whitenoise==6.6.0 
pip install django-cors-headers==4.3.1 asgiref==3.8.1 sqlparse==0.5.0
pip install numpy==1.24.3 Pillow==10.0.1 matplotlib==3.7.1 requests==2.31.0

# ADD THIS LINE FOR OPENCV:
pip install opencv-python==4.8.1.78

echo "Installing lighter PyTorch CPU version..."
pip install torch==1.13.1+cpu torchvision==0.14.1+cpu --index-url https://download.pytorch.org/whl/cpu

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"