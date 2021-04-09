import requests
import json
import jsonlines
import pandas
import os

vi_plus_api_key = os.environ.get('VI_Plus_API_Key')
headers = {'X-Risk-Token': vi_plus_api_key}
cve_list_output_json_file = 'cve_list.json'
output_jsonl_file = 'cves.jsonl'

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def import_cves():
  params = {}
  updated_since = os.environ.get('Updated_Since') 
  if updated_since:
     params['updated_since'] = updated_since

  r = requests.get('https://api.kennasecurity.com/vulnerability_definitions/cve_identifiers', params=params, headers=headers)
  json_cve_ids = r.json()
  cve_ids = json_cve_ids['cve_identifiers']
  print(f'Pulling {len(cve_ids)} CVEs')

  with open(cve_list_output_json_file, 'w') as write_file:
    json.dump(cve_ids, write_file, indent=4, sort_keys=True)

  page_size = 100

  with jsonlines.open(output_jsonl_file, mode='w') as writer:
    cve_ids_page = cve_ids[:page_size]
    cve_ids = cve_ids[page_size:]
    i = 0
    while len(cve_ids_page) > 0:
      r = requests.get('https://api.kennasecurity.com/vulnerability_definitions', params={'cves': ','.join(cve_ids_page)}, headers=headers)
      json_cves = r.json()
      for cve_id, cve_dict in json_cves.items():
        writer.write(cve_dict)
      cve_ids_page = cve_ids[:page_size]
      cve_ids = cve_ids[page_size:]
      i = i+1

if __name__ == '__main__':
    import_cves()
    df = pandas.read_json (r'cves.jsonl', lines=True)
    df.to_json(r'data/vidata.json', orient='records', lines=True)
    df.to_csv(r'data/vidata.csv', index=False)