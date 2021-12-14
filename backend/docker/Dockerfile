FROM --platform=amd64 rust:latest
RUN rustup target add arm-unknown-linux-gnueabihf && \
    git clone https://github.com/raspberrypi/tools $HOME/rpi_tools && \
    mkdir -p /opt/vc/lib
