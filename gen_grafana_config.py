import argparse
import pandas as pd
from jinja2 import Template

parser = argparse.ArgumentParser(description='Generate Grafana JSON config for a station in CHORDS')
parser.add_argument('instrumentID', help='Instrument (i.e. station) ID from CHORDS', type=int)
parser.add_argument('dashboardID', help='Dashboard ID from Grafana JSON config', type=str)
args = parser.parse_args()

instr_id = args.instrumentID
dashboard_id = args.dashboardID

url = r'http://3d.chordsrt.com/instruments'
tables = pd.read_html(url)
df = tables[1].query(f'InstrumentId == {instr_id}')

#print(df)
#quit()

station_name = df.InstrumentName.iloc[1]

print(f'Found station \'{station_name}\' in CHORDS!')

with open('grafana_template.j2') as f:
    content = Template(f.read()).render(
        dashboard_id = dashboard_id,
        station_name = station_name,
        htu21d_temp = int(df.query('VariableShortName == "htu21d_temp"').VariableId),
        htu21d_humidity = int(df.query('VariableShortName == "htu21d_humidity"').VariableId),
        bmp_temp = int(df.query('VariableShortName == "bmp_temp"').VariableId),
        bmp_slp = int(df.query('VariableShortName == "bmp_slp"').VariableId),
        bmp_pressure = int(df.query('VariableShortName == "bmp_pressure"').VariableId),
        mcp9808 = int(df.query('VariableShortName == "mcp9808"').VariableId),
        wind_speed = int(df.query('VariableShortName == "wind_speed"').VariableId),
        wind_direction = int(df.query('VariableShortName == "wind_direction"').VariableId),
        si1145_vis = int(df.query('VariableShortName == "si1145_vis"').VariableId),
        si1145_ir = int(df.query('VariableShortName == "si1145_ir"').VariableId),
        si1145_uv = int(df.query('VariableShortName == "si1145_uv"').VariableId),
        rain = int(df.query('VariableShortName == "rain"').VariableId),
        bmp_altitude = int(df.query('VariableShortName == "bmp_altitude"').VariableId)
    )
    filename = f'{station_name}_grafana_config.json'
    with open(filename, mode="w", encoding="utf-8") as outfile:
        outfile.write(content)
        print(f"Wrote Grafana config to {filename}")

