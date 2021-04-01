import pytest
import testUtils

class myTest():
    def __init__(self):
        print("initData")
        test_data = []
        item = {"provider": "provider1", "name": "name1", "display_name": "display_name1",
                "credentials": "credentials1"}
        test_data.append(item)
        item = {"provider": "provider2", "name": "name2", "display_name": "display_name2",
                "credentials": "credentials2"}
        test_data.append(item)
        item = {"provider": "provider3", "name": "name3", "display_name": "display_name3",
                "credentials": "credentials3"}
        test_data.append(item)
        item = {"provider": "provider4", "name": "name4", "display_name": "display_name4",
                "credentials": "credentials4"}
        test_data.append(item)
        item = {"provider": "provider5", "name": "name5", "display_name": "display_name5",
                "credentials": "credentials5"}
        test_data.append(item)
        testUtils.initdata(test_data, "http://127.0.0.1:5000/addBot")

