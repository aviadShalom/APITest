import requests

def sendAPI(end_point, data,api_method):
    if api_method == 'GET':
        return requests.get(end_point,json=data)
    elif api_method == 'PUT':
        return requests.put(end_point, json=data)
    elif api_method == 'POST':
        return requests.post(end_point, json=data)
    elif api_method == 'PATCH':
        return requests.patch(end_point, json=data)
    elif api_method == 'DELETE':
        return requests.delete(end_point, json=data)
    else:
        return "No Method found"

def initdata(item_list,end_point):
    for item in item_list:
        res = sendAPI(end_point,item,'POST')
        assert res.status_code == 200


def clearData(end_point):
    res = sendAPI(end_point,None, 'POST')
    assert res.status_code == 200