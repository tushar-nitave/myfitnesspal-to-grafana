# myfitnesspal-to-grafana
A web service to export your personal data from myfitnesspal and visualizing the data using grafana dashboard.

## Using the application

1. Clone the repository
2. `python3 -m pip install requirements.txt`
3. `python3 index.py`
4. If you myfitnesspal account and want to export your own data:

    1. Setup your myfitnesspal password by executing:

        `myfitnesspal "your_password" "your username"`
5. If you are not a user you can use nutrition_data.csv file.
6. Go to localhost:5000/ and enter your username and hit get data button. Currently it will retrieve data from Januray 2020 to March 2020.

## Reference
1. https://github.com/coddingtonbear/python-myfitnesspal

## Currently Working On
1. Getting frequency and statistics of frequently eaten foods.
2. Get date range for exporting data