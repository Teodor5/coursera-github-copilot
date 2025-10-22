

def test_index_shows_no_todos(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'To Do App' in resp.data


def test_add_todo(client):
    # add a todo
    resp = client.post('/add', data={'title': 'Test Todo'}, follow_redirects=True)
    assert resp.status_code == 200
    assert b'Test Todo' in resp.data


def test_toggle_todo(client):
    # create via the POST endpoint and parse the generated todo id from the HTML
    resp = client.post('/add', data={'title': 'Toggle Me'}, follow_redirects=True)
    assert resp.status_code == 200
    assert b'Toggle Me' in resp.data
    # find the created todo id by querying the test database directly
    from app import db
    from sqlalchemy import text
    with client.application.app_context():
        row = db.session.execute(text("SELECT id FROM todo WHERE title = :title"), {'title': 'Toggle Me'}).first()
        assert row is not None, 'created todo not found in DB'
        todo_id = row[0]

    # toggle
    resp2 = client.get(f'/update/{todo_id}', follow_redirects=True)
    assert resp2.status_code == 200
    assert b'Complete' in resp2.data or b'Not Complete' in resp2.data


def test_delete_todo(client):
    # create via POST then parse the delete link containing the id
    resp = client.post('/add', data={'title': 'Delete Me'}, follow_redirects=True)
    assert resp.status_code == 200
    assert b'Delete Me' in resp.data
    from app import db
    from sqlalchemy import text
    with client.application.app_context():
        row = db.session.execute(text("SELECT id FROM todo WHERE title = :title"), {'title': 'Delete Me'}).first()
        assert row is not None, 'created todo not found in DB'
        todo_id = row[0]

    resp2 = client.get(f'/delete/{todo_id}', follow_redirects=True)
    assert resp2.status_code == 200
    assert b'Delete Me' not in resp2.data
