# Viper

Viper is a [VI+](https://www.kennasecurity.com/products/vi/) API Enhanced Retrieval tool designed to retrieve large datasets from the [Kenna API](https://apidocs.kennasecurity.com/reference) quickly and efficiently.

## Basic Usage

**Pull The Docker Container:**

```bash
docker pull kennasecurity/viper
```

**Run The Container To Retrive All Vulnerability Definitions:**

```bash
docker run -it \
--env VI_Plus_API_Key=YOURAPIKEYHERE \
--mount type=bind,source="$(pwd)"/data,target=/data \
kennasecurity/viper
```

**Run The Container To Retrive All Vulnerability Definitions Updated Since A Specific Date:**

```bash
docker run -it \
--env VI_Plus_API_Key=YOURAPIKEYHERE \
--env Updated_Since=2021-04-01T00:00:00+0000 \
--mount type=bind,source="$(pwd)"/data,target=/data \
kennasecurity/viper
```

## Advanced Usage

**Clone The Repo:**

```bash
git clone https://github.com/KennaSecurity/Viper
```

**Customize The Python Script:**

In the default configuration VIPER will pull all the vulnerability definitions from the VI+ database and save them in both a [JSON(L)](https://jsonlines.org/) file and a CSV.

You can comment out either of the following lines to limit the output to only the one you need:

```bash
df.to_json(r'data/vidata.json', orient='records', lines=True)
df.to_csv(r'data/vidata.csv', index=False)
```

It is also simple to export this data to any of the other formats that Pandas has a [library](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) for that would be useful in your environment.

**Build The Container:**

```bash
docker build . -t viper
```

**Run The Container To Retrive All Vulnerability Definitions:**

```bash
docker run -it \
--env VI_Plus_API_Key=YOURAPIKEYHERE \
--mount type=bind,source="$(pwd)"/data,target=/data \
viper
```

**Run The Container To Retrive All Vulnerability Definitions Updated Since A Specific Date:**

```bash
docker run -it \
--env VI_Plus_API_Key=YOURAPIKEYHERE \
--env Updated_Since=2021-04-01T00:00:00+0000 \
--mount type=bind,source="$(pwd)"/data,target=/data \
viper
```

## Notes

- A full run pulls over 200,000 vulnerability definitions and takes around 90 minutes to complete.
- Output size of the JSON and CSV will be over 1GB.
- A run for all CVEs update in 2021 took around 5 minutes in April 2020.
