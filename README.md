**Overview**

This is a simple Django application that gets the data from `https://openexchangerates.org/api/` and saves it in the database.
There are apis for currency and exchange_rate. `Get`, `Post`, `Put`, `Patch` and `Delete` methods are all supported.
For `Exchange Rate` api in the application, a sample code to render the data to html also is written - it is commented.

**Note: This is only backend sample application.**

**To get started**

1. Clone the repository.
2. Create virtual environment using `virtualenv`.
3. Navigate to the base folder - `exchange_rates/`
4. Install the requirements from `pip install -r requirements.txt`
5. Install `rabbitmq` and `celery` globally.
6. Create an account in the website of the above url and get the `app_id`.
7. Go to `exchange_rates/exchange_rates/config/.env` and set the variables.
8. Run `rabbitmq-server` and ` celery -A exchange_rates worker -l info` in terminal.
9. Open a new terminal and run `python manage.py runserver 0.0.0.0:8000`.
10. In your browser, navigate to this url - http://localhost:8000/exchange_rates/

**Some Points**
1. A background jobs is created to insert the fetched api data into db. This can be called wherever required. It is asynchronous.
2. The above job will be called when the response from the API is 200 and has content.
   
   1. `ExchangeRateAPI` in `apis.py` has two methods - `get_latest_exchange_rates` and `get_historical_exchange_rates`.
   2. When the response from these is `200`, then a signal is triggered - `exchange_rates_signal`
   3. The above signal in turn triggers - `create_or_update_exchange_rates_data` which creates or updates the data.
   Note: There are other apis in the above website but they are only for paid membership.
   
3. `json` response can be fetched from either postman or in the browser.
4. Two routes are - `exchange_rates/` and `exchange_rates/` - They support all the above said methods.


