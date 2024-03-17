# Install python runtime
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set the working directory
WORKDIR /workdir

# copy requirement.txt from our machine to docker machine work directory
COPY requirements.txt /workdir/

# install python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /workdir/

EXPOSE 8081

# Specify the command to run your UVicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
