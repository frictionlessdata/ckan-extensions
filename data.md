# Data Collection

## Search extensions

First of all, we need to find all the ckan extensions on Github. We're going to look at all the repos having `ckanext` in its name. Github Search API has quite strict querying limits so we have to use different techniques to avoid rate limit errors. As a high-level data collections framework, we will use Frictionless Transform. It will sort the packages by repository's stargazers count and save it to the CSV file:

```bash
$ python code/search.py
```

```python file
code/search.py
```
