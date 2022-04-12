FROM python:3

# Update system and install system needs
# RUN apt-get update -y \
#     && apt-get install -y awscli default-jre \
#     && aws --version

RUN apt-get update -y \
    && apt-get install -y default-jre

# OpenDcs Version
ENV OPENDCS_VERSION=6-5-RC03 \
    PATH=/app/opendcs/bin:$PATH \
    DCSTOOL_HOME=/app/opendcs \
    LRGSHOME=$DCSTOOL_HOME/app/opendcs/lrgs

RUN mkdir -p -m 775 /git ${DCSTOOL_HOME} ${LRGS_HOME} /opendcs_logs /opendcs_output

# Create User
RUN useradd -u 1500 -d ${DCSTOOL_HOME} opendcs

WORKDIR /app/opendcs/lrgs

# Install OpenDcs
COPY ./builds/opendcs-cwms-${OPENDCS_VERSION}.tar.gz /
RUN tar zxf /opendcs-cwms-${OPENDCS_VERSION}.tar.gz -C /app \
    && rm /opendcs-cwms-${OPENDCS_VERSION}.tar.gz

# Overwrite decodes.properties and chown to opendcs
COPY ./lrgs ${DCSTOOL_HOME}/lrgs
COPY ./bin/startLRGS ${DCSTOOL_HOME}/bin/

# Now make opendcs the owner of all things DCS
RUN chown -R opendcs:opendcs  /app /opendcs_logs /opendcs_output

COPY ./entrypoint.sh /

# RUN chmod +x /entrypoint.sh

# VOLUME [ "/git" ]
# VOLUME [ "/opendcs_logs" ]
# VOLUME [ "/opendcs_output" ]

ENTRYPOINT ["/entrypoint.sh"]

USER opendcs