# Prometheus metrics exporter 1.0

Export metrics from Prometheus in Graphite format.

## Usage.

Clone repository and run from his directory.

`PrometheusMetricsExporter:> prometheus-metrics-exporter.sh`

## Options

Configuration reads from file config/config.yml.

## Docker

You may download [Docker image](https://hub.docker.com/repository/docker/alexwolf1975/prometheus-metrics-exporter) for familiarization.

To use your self configuration use run like below.

`PrometheusMetricsExporter:> docker run -v ~/PrometheusMetricsExporter/config:/PrometheusMetricsExporter/config prometheus-metrics-exporter:latest`

## Testing

To test connection to reciever you may use command line tools and look at list of metrics.

`:> nc -lv 2003`
