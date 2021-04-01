import pytest
import sys
import testUtils
from serverConfig import myServer
import pdb

t = myServer()


# def test_initData():
#     print("initData")
#     test_data = []
#     item = {"provider": "provider1", "name": "name1","display_name":"display_name1","credentials":"credentials1"}
#     test_data.append(item)
#     item = {"provider": "provider2", "name": "name2", "display_name": "display_name2", "credentials": "credentials2"}
#     test_data.append(item)
#     item = {"provider": "provider3", "name": "name3", "display_name": "display_name3", "credentials": "credentials3"}
#     test_data.append(item)
#     item = {"provider": "provider4", "name": "name4", "display_name": "display_name4", "credentials": "credentials4"}
#     test_data.append(item)
#     item = {"provider": "provider5", "name": "name5", "display_name": "display_name5", "credentials": "credentials5"}
#     test_data.append(item)
#     testUtils.initdata(test_data,"http://127.0.0.1:5000/addBot")
#
#
def test_GetItemWithGet():
    provider_name = "provider3"
    api_url = "{}bots/{}".format(t.BASE_API,provider_name)
    api_method = 'GET'
    res = testUtils.sendAPI(api_url,None,api_method)
    assert res.status_code == 200
    p = res.json()
    assert p["provider"] == provider_name


def test_GetItemWithPOST():
    provider_name = "provider2"
    api_url = "{}bots/{}".format(t.BASE_API, provider_name)
    api_method = 'GET'
    res = testUtils.sendAPI(api_url, None, api_method)
    assert res.status_code == 200
    p = res.json()
    assert p["provider"] == provider_name


def test_AddItem():
    test_data = {"provider": "provider7", "name": "name7", "display_name": "display_name7",
                    "credentials": "credentials7"}

    api_url = "{}bots/".format(t.BASE_API)
    api_method = 'PUT'
    res = testUtils.sendAPI(api_url, test_data, api_method)
    assert res.status_code == 200

    api_url = "{}bots/{}".format(t.BASE_API,test_data['provider'])
    api_method = 'GET'
    res = testUtils.sendAPI(api_url, None, api_method)
    assert res.status_code == 200
    p = res.json()
    assert (p == test_data)


def test_PatchItem():
    test_data = {"provider": "provider5", "name": "name5 New", "display_name": "display_name5 New",
                 "credentials": "credentials555 New"}

    api_url = "{}bots/provider5".format(t.BASE_API)
    api_method = 'PATCH'
    res = testUtils.sendAPI(api_url, test_data, api_method)
    assert res.status_code == 200
    api_url = "{}bots/{}".format(t.BASE_API, test_data['provider'])
    print(api_url)
    api_method = 'GET'
    res = testUtils.sendAPI(api_url, None, api_method)

    assert res.status_code == 200
    p = res.json()
    assert (p == test_data)

def test_DeleteItem():
    api_url = "{}bots/provider4".format(t.BASE_API)
    api_method = 'DELETE'
    res = testUtils.sendAPI(api_url, None, api_method)
    assert res.status_code == 200

    api_method = 'GET'
    res = testUtils.sendAPI(api_url, None, api_method)
    assert res.status_code == 403 and res.text == "Item Not Found"


# negative tests
def test_DeleteItemFail():
    api_url = "{}bots/provider42".format(t.BASE_API)
    api_method = 'DELETE'
    res = testUtils.sendAPI(api_url, None, api_method)
    assert res.status_code == 403 and res.text == "Item Not Found"


def test_AddItemFail():
    test_data = {"provider": "provider2", "name": "name2", "display_name": "display_name2",
                 "credentials": "credentials2"}

    api_url = "{}bots/".format(t.BASE_API)
    api_method = 'PUT'
    res = testUtils.sendAPI(api_url, test_data, api_method)
    assert res.status_code == 403 and res.text == "item already exists"

def test_PatchItemFail():
    test_data = {"provider": "provider66", "name": "name666 New", "display_name": "display_name6666 New",
                 "credentials": "credentials66 New"}

    api_url = "{}bots/provider66".format(t.BASE_API)
    api_method = 'PATCH'
    res = testUtils.sendAPI(api_url, test_data, api_method)
    assert res.status_code == 403 and res.text == "Item Not Found"