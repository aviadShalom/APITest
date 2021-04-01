import testUtils

class myServer():
    BASE_API = "http://127.0.0.1:5000/"
    SAMPLE_DATA = [{"provider": "provider1", "name": "name1", "display_name": "display_name1",
                "credentials": "credentials1"},
                   {"provider": "provider2", "name": "name2", "display_name": "display_name2",
                    "credentials": "credentials2"},
                   {"provider": "provider3", "name": "name3", "display_name": "display_name3",
                    "credentials": "credentials3"},
                   {"provider": "provider4", "name": "name4", "display_name": "display_name4",
                    "credentials": "credentials4"},
                   {"provider": "provider5", "name": "name5", "display_name": "display_name5",
                    "credentials": "credentials5"}
    ]

    def __init__(self):
        print("initData")
        testUtils.clearData("{}clearData".format(self.BASE_API))
        testUtils.initdata(self.SAMPLE_DATA, "{}addBot".format(self.BASE_API))
