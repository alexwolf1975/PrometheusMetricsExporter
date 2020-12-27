FROM ubuntu:20.04

RUN apt-get update

RUN apt-get -y install bash netcat-openbsd python3-yaml wget

COPY . /PrometheusMetricsExporter

WORKDIR /PrometheusMetricsExporter

RUN chmod a+x prometheus-metrics-exporter.sh

ENTRYPOINT ["./prometheus-metrics-exporter.sh"]
