# Every Politician Data List


This is a python script to download the list of politicians from 233 countries available on the website [EveryPolitician](http://everypolitician.org).


## EveryPolitician Data

EveryPolitician is a project to collect and share data, in a consistent, open format that anyone can use. Their dataset contains informatio about over 70,000 politicians from 233 countries so far.
Data is freely available for everybody to use. Data can be downloaded from their website in two formats:

* CSV format
* JSON format

## The script

The script downloads the JSON file containing the list of countries and the JSON files containing the list of politicians. Their details are:

* Country (country)
* Legislatures name (legislatures name)
* Number of politicians elected in the legislatures (person count)
* Link to JSON containing the list (url json)
* Politician's name (politician name)
* Link to web profile, if present (politician link)

Two scripts have been created:

* get_list_politicians.py downloads the list of politicians into an Excel file
* get_politicians_csv.py downloads the list of politicians into a CSV file
