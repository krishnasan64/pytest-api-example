from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

@pytest.fxture
def order_update_payload();
return{
    "petId":1,
    "status":"approved"
}
def test_patch_order_by_id(order_update_payload):
    order_id=1
    test_endpoint = f"/store/order/{order_id}"
    response=api_helpers.patch_api_data(test_endpoint,order_update_payload)
    assert_that(response.status_code,is_(200))
    body=response.json()
    assert_that(body["message"],contains_string("Order and pet status updated successfully"))
