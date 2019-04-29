# smile-widget-code-challenge

The Smile Widget Company currently sells two types of smile widgets: a Big Widget and a Small Widget.  We'd like to add more flexibility to our product pricing.

## Setup with Docker
1. Install Docker (https://docs.docker.com/install/)
2. Clone this repository.
3. `>>> docker-compose up --build`

## Setup without Docker
1. Install Python (>3.4)
2. Install postgres.  By default the Django app will connect to the database named 'postgres'.  See `settings.DATABASES`.
3. Clone this repository.
4. Install requirements.
  * `>>> pip install -r requirements.txt`
5. Run migrations.
  * `>>> python manage.py migrate`
6. Load data from fixtures:
  * `>>> python manage.py loaddata 0001_fixtures.json`

### Technical Requirements
* We currently have to products with the following prices:
    * Big Widget - $1000
    * Small Widget - $99
* These products, along with existing gift cards are already setup in the database.  Study the existing models and initial data.
* Create a new ProductPrice model and setup the following price schedule:    
  * Black Friday Prices (November 23, 24, & 25)
    * Big Widget - $800
    * Small Widget - FREE!
  * 2019 Prices (starting January 1, 2019)
    * Big Widget - $1200
    * Small Widget - $125
* Build a JSON API endpoint that accepts a product code, date, and (optional) gift card and returns product price.
  * The endpoint should live at `api/get-price` and accept the following parameters:
    * `"productCode"`
    * `"date"`
    * `"giftCardCode"`
* Update this README file with instructions on how to run and access your price calculator.
* Create a pull request with your changes.

### Task of adding special Prices added, Api created
* follow above steps
* Run server
* open the following urls to see the functionality of ProductPrice
    * big widget without any offer
      * http://127.0.0.1:8000/api/get-price/big_widget/2018-11-20/
    * big widget with Black Friday offer
      * http://127.0.0.1:8000/api/get-price/big_widget/2018-11-23/
      * http://127.0.0.1:8000/api/get-price/big_widget/2018-11-24/
    * big widget with 2019 Prices
      * http://127.0.0.1:8000/api/get-price/big_widget/2019-05-20/

    * Small Widget without any offer
      * http://127.0.0.1:8000/api/get-price/sm_widget/2018-11-20/
    * Small Widget with Black Friday offer
      * http://127.0.0.1:8000/api/get-price/sm_widget/2018-11-23/
      * http://127.0.0.1:8000/api/get-price/sm_widget/2018-11-24/
    * Small Widget with 2019 Prices
      * http://127.0.0.1:8000/api/get-price/sm_widget/2019-05-20/

* open the following urls to see the functionality of giftCardCode
    * big widget with 250OFF
      * http://127.0.0.1:8000/api/get-price/big_widget/2018-12-01/?giftCardCode=250OFF
    * Small Widget with 250OFF
      * http://127.0.0.1:8000/api/get-price/sm_widget/2018-12-01/?giftCardCode=250OFF

* you can try different combinations
* also can apply giftcard code to the discount prices but be clear the dates are matched in both GiftCard and ProductPrice tables 

### Additional Information
* Please use Django Rest Framework or a Python web framework of your choice to create the endpoint.
* Just as a general guideline, we've designed this exercise to take less than 4 hours.
