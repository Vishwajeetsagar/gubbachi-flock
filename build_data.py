# Turns data/students.xlsx into data.json  (student NAMES are removed on purpose)
import pandas as pd, json, glob, datetime
d = pd.read_excel(sorted(glob.glob('data/*.xlsx'))[-1])
rows = [[r.School, r.Program, str(r.Grade), r.Gender,
         r.Enrolled.strftime('%Y-%m') if pd.notna(r.Enrolled) else ''] for r in d.itertuples()]
json.dump({'updated': datetime.date.today().isoformat(), 'rows': rows}, open('data.json', 'w'), separators=(',', ':'))
print(len(rows), 'rows written to data.json')
