############################################################
# Dockerfile to build a Slocker container
# Based on Python 2.7
############################################################

# Set the base image
FROM python:2.7

# File Author / Maintainer
MAINTAINER Andre Lobato <andrefelipelobato@gmail.com>

# Create app folder, where the magic is !
RUN mkdir -p /usr/lib/Slocker

# Copy the application folder inside the container
COPY . /usr/lib/Slocker

# Install requirements
RUN pip install -r /usr/lib/Slocker/requirements.txt

# Set the default directory where CMD will execute
WORKDIR /usr/lib/Slocker/slocker

CMD python slocker.py

# Expose port
EXPOSE 8080