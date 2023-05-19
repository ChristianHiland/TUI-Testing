FROM gitpod/workspace-full

# Install Wine dependencies
RUN sudo dpkg --add-architecture i386 && \
    sudo apt-get update && \
    sudo apt-get install -y wine wine32

# Set environment variables
ENV WINEPREFIX=/home/gitpod/.wine
ENV WINEARCH=win32
