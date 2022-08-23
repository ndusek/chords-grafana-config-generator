# Grafana JSON config generator for NCAR 3D CHORDS platform

A simple Python script and Jinja2 template that automatically generates a Grafana JSON config from a station ID in CHORDS.

## Installation

Clone the repo.

```
git clone https://github.com/ndusek/chords-grafana-config-generator.git
cd chords-grafana-config-generator
```

Optionally create a virtual environment to isolate dependencies.

```
python3 -m venv chords
source chords/bin/activate
```

Install dependencies.

```
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Generating a config

Help menu:

```
python3 gen_grafana_config.py -h
```

```
usage: gen_grafana_config.py [-h] instrumentID dashboardID

Generate Grafana JSON config for a station in CHORDS

positional arguments:
  instrumentID  Instrument (i.e. station) ID from CHORDS
  dashboardID   Dashboard ID from Grafana JSON config

optional arguments:
  -h, --help    show this help message and exit
```

Example:

```
python3 gen_grafana_config.py 94 0YAdYui4z
```

Output:

```
Wrote Grafana config to NDSU_03_grafana_config.json
```

