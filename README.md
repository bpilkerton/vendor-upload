# vendor-upload

# Problem

# Solution

# Install vendor-upload app and dependencies
```
git clone https://github.com/bpilkerton/vendor-upload.git
cd vendor-upload
```

## And the virtualenv...
```
sudo pip3 install virtualenv
virtualenv -p /usr/bin/python3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

# Run the app
```
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

# What's happening here?
