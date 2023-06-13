# Constructing the Portrait-Sitting Database Website 

The Portrait-Sitting Database website (www.portrait-sitting.co.uk) is one product of a 3-month placement with the Knowledge Media Institute. The aim of the placement project was to develop a method of publishing structured data (specifically, RDF linked data) in a user-friendly website format. I used my own research data, on the subject of portraiture and the portrait sitting, as a case study for this work.

I constructed the Portrait-Sitting Database website in five stages:

1.	I transformed my spreadsheet data into RDF, using SPARQL Anything (https://sparql-anything.cc/).
2.	I inferred additional data, using the HermiT reasoner in Protege (https://protege.stanford.edu/).
3.	I transformed the RDF data back into a spreadsheet format, using SPARQL Anything.
4.	I generated a website to display the spreadsheet data, using Jinja and Bootstrap (https://jinja.palletsprojects.com/en/3.1.x/; https://getbootstrap.com/).
5.	I generated static files from the dynamic website, using PowerShell.

Steps 1, 2 and 3 may be considered pre-requisites for the construction of a database website, since they pertain to the completeness of the data. Therefore, my documentation focuses on steps 4 and 5. The documentation includes:

- In 'spreadsheets': The headers for the spreadsheet data that I used to generate the dynamic website in step 4.
- In 'application': The Jinja application that I used to generate the dynamic website in step 4.
- In 'templates': The Jinja templates that I used to generate the dynamic website in step 4.
- Below: Step-by-step instructions for generating the dynamic website, using the spreadsheets, application and templates.
- Below: Step-by-step instructions for using the dynamic website to generate the static website.
- At https://www.oocdtp.ac.uk/news: An account of the reasons for choosing this method and the experience of the placement (coming soon).

The documentation assumes a Windows operating system.

## Generating the dynamic website (step 4)

```
#Create a folder 'DynamicSite'. This will be the location of the Jinja application and spreadsheets.

#Create a sub-folder 'DynamicSite\templates'. This will be the location of the Jinja templates.

#Create a sub-folder 'DynamicSite\static' and a further sub-folder 'DynamicSite\static\img'.

#Create a virtual environment 'DynamicSite\venv'
> py -3 -m venv venv

#Activate the virtual environment
> venv\Scripts\activate

#Install flask, pandas, openpyxl
> pip install flask
> pip install pandas
> pip install openpyxl

#Run the Jinja app
> python __init__.py

```

## Generating the static website (step 5)

```
#Create a folder 'StaticSite'. This will be the location of the static website.

#Create sub-folders 'StaticSite\account', 'StaticSite\artobject', 'StaticSite\artobjectrole', 'StaticSite\event', 'StaticSite\eventrole', 'StaticSite\informationobject', 'StaticSite\object', 'StaticSite\objectrole', 'StaticSite\record', 'StaticSite\source', 'StaticSite\term'

#Create a copy of 'DynamicSite\static', 'StaticSite\static'

#Create a file 'StaticSite\log.txt'. This will contain a list of html files that could not be generated. 

#In PowerShell:
>$req = Invoke-WebRequest -uri 'http://localhost:5000/test.html'
>$pages=$req.Links
>$pglinks=$req.Links | Select -ExpandProperty href
>$fullpglinks=foreach ($pglink in $pglinks) {write-output('http://localhost:5000'+$pglink+'.html')}
>foreach ($fullpglink in $fullpglinks){
try {
Invoke-WebRequest -uri $fullpglink -outfile ('StaticSite\'+$fullpglink.Replace('http://localhost:5000','').Replace('/','\'))}
catch {add-content -path StaticSite\log.txt -Value $fullpglink}
}         

```