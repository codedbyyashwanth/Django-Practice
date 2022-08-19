from django.shortcuts import render

data = [
        "Heading One",
        "Heaiding Two"
]

datas = [
        { "id": 1, "value": "This is in first index" },
        { "id": 2, "value": "This is in second index" },
        { "id": 3, "value": "This is in third index" },
]

def Home(request):
        return render(request, "base/home.html", {"data" : datas})

def App(request, id):
        value = None
        for data in datas:
                if data['id'] == int(id):
                        value = data
        context = { "data" : value }
        return render(request, "base/store.html", context)