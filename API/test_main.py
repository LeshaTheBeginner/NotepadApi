from fastapi.testclient import TestClient
import json
from main import app
import uuid

client = TestClient(app)

# please note that this whole test assumes that the last note edited/created/deleted/recovered is the test note
def test_read_get_notes():
    response = client.get("/getnotes")
    assert response.status_code == 200
    assert response.json != None

def test_create_note():
    global test_name
    test_name = str(uuid.uuid4)
    response = client.post("/create", headers={"Content-Type" : "application/json"}, json={"notename":test_name,"noteowner":"TEST_MAIN.PY","notedata":"THIS IS A TEST","notetype":"txt"})
    assert response.status_code == 200

def test_lastcreated():
    global test_name
    global test_note
    response = client.get("/lastcreated")
    assert response.status_code == 200
    test_note = response.json()
    assert test_note["notename"] == test_name
    assert test_note["noteowner"] == "TEST_MAIN.PY"
    assert test_note["notedata"] == "THIS IS A TEST"
    assert test_note["notetype"] == "txt"
    assert test_note["favorite"] == False
    # assert response.json == {"noteid":"8884695c-0545-4c46-9958-159c02cc9073","notename":"TEST","noteowner":"TEST_MAIN.PY","notedata":"THIS IS A TEST","notetype":"txt","favorite":false,"notecreatedate":"2026-06-27T12:02:21.395909","noteeditdate":"2026-09-13T18:04:10.045831"}

def test_star_note():
    global test_note
    id = test_note["noteid"]
    id = str(id)
    # temp = '{"noteid":{test}}'.format("test",id)
    response = client.post("/star", headers={"Content-Type" : "application/json"}, json={"noteid": id})
    assert response.status_code == 200
    response = client.get("/lastcreated")
    assert response.status_code == 200
    test_note = response.json()
    assert test_note["favorite"] == True

def test_search_note():
    global test_note
    response = client.post("/search", headers={"Content-Type" : "application/json"}, json={"search_query":test_note["notename"][:5]})
    assert response.status_code == 200
    test_search = response.json()
    if test_note in test_search:
        assert True

def test_edit_note():
    global test_note
    response = client.post("/edit", headers={"Content-Type" : "application/json"}, json={"noteid":str(test_note["noteid"]),"notedata":"Testing /edit note."})
    assert response.status_code == 200
    test_note["notedata"] = "Testing /edit note."
    response = client.get("/lastcreated")
    assert response.status_code == 200
    edited_note = response.json()
    assert edited_note["noteowner"] == test_note["noteowner"]
    assert edited_note["notedata"] == test_note["notedata"]

def test_delete_note():
    global test_note
    response = client.post("/delete", headers={"Content-Type" : "application/json"}, json={"noteid": str(test_note["noteid"])})
    assert response.status_code == 200
    response = client.get("/lastcreated")
    assert response.status_code == 200
    assert str(response.json()["noteid"]) == "00000000-0000-0000-0000-000000000000"
    assert response.json()["notedata"] == test_note["notedata"]

def test_restore_note():
    global test_note
    response = client.get("/restore")
    assert response.status_code == 200
    response = client.get("/lastcreated")
    assert response.status_code == 200
    assert response.json()["noteowner"] == test_note["noteowner"]
    assert response.json()["notedata"] == test_note["notedata"]
    test_note["noteid"] = response.json()["noteid"]

def test_perm_delete_note():
    global test_note
    response = client.post("/delete", headers={"Content-Type" : "application/json"}, json={"noteid": str(test_note["noteid"])})
    assert response.status_code == 200
    response = client.get("/lastcreated")
    assert response.status_code == 200
    assert str(response.json()["noteid"]) == "00000000-0000-0000-0000-000000000000"
    assert response.json()["notedata"] == test_note["notedata"]
    response = client.post("/delete", headers={"Content-Type" : "application/json"}, content='{"noteid": "00000000-0000-0000-0000-000000000000"}')
    assert response.status_code == 200
    response = client.post("/search", headers={"Content-Type" : "application/json"}, json={"search_query":test_note["notename"]})
    assert response.status_code == 200
    test_search = response.json()
    for i in test_search:
    # TODO: What if the noteid changed? This sure won't catch it
        if test_note["notename"] in i[1]:
            assert False
            break
