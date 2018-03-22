FROM bpack/todobackend-base:latest
MAINTAINER Benjamin Pack <ben.pack@gmail.com>

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python-dev libmysqlclient-dev

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    pip install wheel --upgrade

# PIP Environment variables (must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# Output: Build artifacts (Wheels) are output here
VOLUME /wheelhouse

# Output: Build cache for pip
VOLUME /build

# Output: Test reports are output here
VOLUME /reports

# Test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python", "manage.py", "test", "--noinput"]

# Add application source. This layer is what will typically get rebuilt
COPY src /application
WORKDIR /application
