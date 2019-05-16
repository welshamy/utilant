# Utilant Head of Machine Learning Exercise

This git repository includes all the files and information related to this exercise.

## Loading the data in a cloud DB

The data source on the cities website is refreshed on a daily basis.  It can be automatically consumed by calling their API or downloading the entire file (inefficient if done daily) and loading it into a DB of our choice.

I chose [AWS Elastic Map Reduce (EMR)](<https://aws.amazon.com/emr/>), and used Apache Hive, for a few reasons:

1. It can query the data with a SQL dialect using Apache Hive.
2. Refreshing the data is easy.  Just dump a text file with the new records in the table's directory.
3. It satisfies our On-line Analytical Processing (OLAP) requirements.  Relatively low volume of transactions with complex queries on huge volumes of data.  The query execution time lag is not a big concern in this analytical database, unlike transactional ones.
4. Changing the data model does not require rebuilding the entire DB.  We may even have multiple data models overlaid simultaneously on top of the same data files to satisfy different needs.

You can run a sample query on the cleaned and normalized Chicago data set by logging into the EMR cluster as follows and use the password I included in my email:

```
$ ssh utilant@ec2-3-210-204-82.compute-1.amazonaws.com
```

Next, run hive and execute a query as shown below:

```
$ hive
Logging initialized using configuration in file:/etc/hive/conf.dist/hive-log4j2.properties Async: false
hive> SELECT facility_name, inspection_date, results, violations
FROM utilant_food
WHERE inspection_date>='2019-01-01' and results='Fail';
```



## Data analysis, cleaning and insights

Review the Jupyter notebook `food_inspection.ipynb` which includes exploratory data analysis and data cleaning and normalization for the Chicago data set.  A couple of insights were also drawn from that data set.

Since food safety health inspection regulations vary by city, the three data sets (Chicago, Las Vegas, New York) have a handful of features in common.  They share about one third of the entire feature set, usually with different feature names.  Some common features, like the results of inspection, have different values in different data sets.  In Chicago, it takes values of `Pass`, `Pass w/Conditions`, or `Fail`.  In New York, we have a letter grade `A,B,C,Z,P` and a numerical value [1,...,136].  In Las Vegas, we have a letter grade `A,B,C,X,P,O` and over a dozen categorical `Inspection Result` values.

We can build a machine learning model that predicts the likelihood of a restaurant failing its city food inspection.  However, every city needs to have its own model for a few reasons:  1) To make the best use of the features unique to each city.  2) Every city has it's own food safety code and different ways of enforcing it.

## Micro-service for a mock ML model

I created a Flask REST API in the `food_inspection.py` file.  When deployed locally or to production, it runs a micro-service that mocks a machine learning model predicting the likelihood of passing an inspection.  If the restaurant name begins with a letter in (r,s,t,l,n,e), it returns a JSON response with a likelihood of 0.  Otherwise, it returns a response with likelihood of 1.
