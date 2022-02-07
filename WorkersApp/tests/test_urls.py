from django.urls import resolve, reverse


class TestUrls:
    def test_home_url(self):
        path = reverse("home")
        assert resolve(path).view_name == "home"

    def test_create_url(self):
        path = reverse("worker-create")
        assert resolve(path).view_name == "worker-create"

    def test_list_url(self):
        path = reverse("worker-list")
        assert resolve(path).view_name == "worker-list"

    def test_detail_url(self):
        path = reverse("worker-detail", kwargs={"pk": 1})
        assert resolve(path).view_name == "worker-detail"

    def test_update_url(self):
        path = reverse("worker-update", kwargs={"pk": 1})
        assert resolve(path).view_name == "worker-update"

    def test_delete_url(self):
        path = reverse("worker-delete", kwargs={"pk": 1})
        assert resolve(path).view_name == "worker-delete"

    def test_csv_url(self):
        path = reverse("workers-csv")
        assert resolve(path).view_name == "workers-csv"
