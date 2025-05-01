
from Utilities.TestUtilities import TestUtilities

class Test_Inheritance(TestUtilities):
    def test_userstatus(self):
        user_data={"name":"Priyanka", "status": "active"}
        self.assert_status(user_data["name"],"Priyanka")
        self.log(f"Hello, {user_data['name']}!")


