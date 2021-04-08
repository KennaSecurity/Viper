# Viper

Viper is a [VI+](https://www.kennasecurity.com/products/vi/) API Enhanced Retrvial tool designed to retrieve large datasets from the [Kenna API](https://apidocs.kennasecurity.com/reference) simple.

## Configuration and Customization

In the default configuration VIPER will pull all the CVES from the VI+ database and save them in both a JSON(L) file and a CSV.

You can edit this date line to only pull CVEs that were updated in the AP after the stated date:

`updated_since = '2000-01-01T00:00:00+0000'`

You can comment out either of the following lines to limit the output to only the one you need:

`df.to_json(r'data/vidata.json', orient='records', lines=True)`

`df.to_csv(r'data/vidata.csv', orient='records', index=False)`

It is also simple to export this data to any of the other formats that Pandas has a [library](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) for that would be useful in your enviroment.

## Usage

Update  `updated_since` in the viper script to limit the CVEs to pull or commment it out to pull all data.

Build Contaier:
`docker build . -t viper`

Run Container:
`docker run -it -e VI_PLUS_API_KEY=YOURAPIKEYHERE--mount type=bind,source="$(pwd)"/data,target=/data  viper`

## Notes

- A full run pulles over 200,000 CVEs and takes around 90 minutes to complete.
- Output size of the JSON and CVE will be over 1GB.
- A run for all CVEs update in 2021 took around 5 minutes in April 2020.
