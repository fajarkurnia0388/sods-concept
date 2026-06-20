FROM python:3.12-slim

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.lock /app/
RUN pip install --no-cache-dir -r requirements.lock

# Copy the rest of the project
COPY . /app/

# Install the package itself
RUN pip install --no-cache-dir .

# Set default command to show CLI help
CMD ["sods", "--help"]
