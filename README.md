# vendor-upload

# Problem
We need a way for our subscription fulfillment vendor to deliver subscriber data to the organization. They will deliver uncompressed TSV files to us via a simple file upload process. Create a web application to facilitate this process.

# Solution
For this solution, I built a simple django application which relies heavily on the built-in admin interface. To keep things simple, a sqlite database is used. My goal was to deliver a solution that actually works but it comes with some sacrifices. Read below for issues with this implementation and recommended steps on deploying to a real world environment.

## Install the vendor-upload app and dependencies
```
git clone git@github.com:bpilkerton/vendor-upload.git
cd vendor-upload
```

## And the virtualenv...
```
sudo pip3 install virtualenv
virtualenv -p /usr/bin/python3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Run the app
```
cd src
python manage.py runserver
```

Note: I've created a couple of users already; a super user called `atlanticadmin` and a simulated vendor user called `vendor`:

```
Superuser: atlanticadmin/f$ls.aiarC,
Vendor User: vendor/d@taDeliV3ry
```

1. Open a browser to `http://127.0.0.1:8000` and sign in using the Vendor login above.
2. Select `+Add` next to Upload to upload a new file
3. Select the test file and select `Save`
4. Select `Vendor Datas` on the left navigation to view the imported records

From here, one can edit the properties of individual records or manually add/delete records.
Or you can query the database directly doing something like:

```
sqlite3 db.sqlite3

sqlite> select * from upload_upload;
1|vendor_uploads/sample-data.txt|2021-01-27 22:52:08.139384

sqlite> select * from upload_vendordata;
1|1|Snake|Plisken|123 Fake St.|AZ|12345|new|432|Masthead|100.12|2007-04-05
2|1|Snake|Plisken|123 Fake St.|AZ|12345|canceled|432|Masthead|100.12|2007-04-06
3|2|Clark|Kent|456 Fake St.|CA|54321|new|431|Print Magazine|50.12|2007-04-07
4|3|Johnny|Johnson|789 Not Real St.|OH|45321|new|431|Print Magazine|50.12|2007-04-08
5|3|Johnny|Johnson|789 Not Real St.|OH|45321|canceled|431|Print Magazine|50.12|2007-04-08
...
```
## What are the problems with this approach?

* The database is not normalized. If I had the time I would update the model and add these tables
    * User table -- first_name, last_name etc
    * Products table -- product_id, product_name, product_price
    * Transactions table -- relations to User and Product, status etc
* The application doesn't do any checks on the uploaded file. All user input should not be trusted. I'd enforce certain file extensions and mime types, potentially run the file through an antivirus engine etc
* There are no tests! I'd add tests to enforce data integrity on the uploaded file as well as the application itself.
* No data sanitization or normalization of the tsv data itself

## How I'd deploy something like this in the real world

In the real world, this application wouldn't do so well running on the built-in Django webserver. In the past I've used these tools to deploy to production:

* gunicorn - a WSGI server to run the app with multiple workers
* supervisord - a program to manage the service and ensure uptime
* nginx - a reverse proxy to serve client requests and talk to the backend server
* rabbitmq/celery - message queue to initiate the processing of files and tasks

https://data.chronicle.com and https://aldaily.com are example implementations in production.

