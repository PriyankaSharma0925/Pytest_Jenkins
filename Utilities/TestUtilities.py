class TestUtilities:

    def assert_status(self, actual, expected):
        assert expected in actual

    def log(self, message):
        print(f"LOG {message}")
