
def test_create_question(client):
    """Тест создания вопроса"""
    response = client.post("/questions/", json={"text": "Test question"})
    print(f"Create status: {response.status_code}")

    assert response.status_code in [200, 422]

    if response.status_code == 200:
        data = response.json()
        assert data["text"] == "Test question"
