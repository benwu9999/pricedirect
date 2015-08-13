def get_service():
    """returns an initialized and authorized bigquery client"""

    from googleapiclient.discovery import build
    from oauth2client.client import GoogleCredentials

    credentials = GoogleCredentials.get_application_default()
    if credentials.create_scoped_required():
        credentials = credentials.create_scoped(
            'https://www.googleapis.com/auth/bigquery')
    return build('bigquery', 'v2', credentials=credentials)