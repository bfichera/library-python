from nutritionix.nutritionix import NutritionixClient
import logging

logging.basicConfig(level=logging.DEBUG)
 
nutritionix = NutritionixClient(
    application_id='APP_ID',
    api_key='API_KEY',
    # debug=True, # defaults to False
)

# A cherry coke bottle
q = nutritionix.item(upc='049000018011')
print(q)
