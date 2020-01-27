# NDC-National-Drug-Code-Lookup
A Python script for looking up drug facts and information by NDC code. Quickly search and map a drug name with an NDC code. 

### Usage
* `search_ndc_database(NDC)` takes in a string NDC. 
  * example: `search_ndc_database('233215')`
  * returns: Proprietary Name, Non-Proprietary Name, Dosage Form, Route Name, Company Name, Product Type
 
### How It Works
* Utilizing request & beautiful soup, this script takes the "data-title" tag - example for Proprietary Name of a given NDC code `str(soup.findAll("td", {"data-title": "Proprietary Name"})[0])` - from the html of ndclist.com and returns a list of results
