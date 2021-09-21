import src.google_search_origin as google_search_origin

if __name__ == '__main__':
    google = google_search_origin.GoogleSearchOrigin(search='dog', request_cooldown=0.1)
    google.request_url()
    print(google.get_all_links())
    google.request_url()
    print(google.get_all_links())