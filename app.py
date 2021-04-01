from flask import Flask,request, jsonify,Response

app = Flask(__name__)

data = []



@app.route("/clearData",methods=["POST"])
def clearData():
    data.clear()
    print("Data cleared")
    return Response("Data cleared successfully ", status=200)

@app.route("/addBot",methods=["POST"])
def botobject():
    content = request.json
    print(data)
    if content is None:
        return Response("Invalid request please include json", status=403)

    if 'provider' not in content:
        return Response("Invalid Json fields",status=403)

    data.append(content)

    return Response("Operation completed successfully ",status=200)


@app.route("/bots/<provider>",methods=['PUT','PATCH','GET','DELETE','POST'])
@app.route("/bots/",defaults={'provider': None},methods=['PUT','PATCH','GET','DELETE','POST'])
def getitem(provider):
    print(data)
    content = request.json

    if request.method != 'PUT':
        if provider is None:
            return Response("Invalid request missing provider",status=403)
    else:
        provider = content['provider']

    for item in data:
        if item['provider'] == provider:
            if request.method == 'DELETE':
                data.remove(item)
                return Response("item removed", status=200)

            elif request.method == 'PATCH':
                data.remove(item)
                data.append(content)
                return Response("item updated", status=200)
            elif request.method in ['GET', 'POST']:
                return jsonify(item)
            else:
                return Response("item already exists",status=403)
    if request.method == 'PUT':
        data.append(content)
        return Response("Item added", status=200)

    return Response("Item Not Found",status=403)




if __name__ == "__main__":
    print("start")
    app.run()