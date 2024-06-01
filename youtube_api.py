
import requests

API_KEY = 'AIzaSyA2nXFQrdw0tNPkyDp1_XGMBp8n6t8p0ek'
VIDEO_IDS = ['fOdnfAaK8QM', 'fyTBaWGa-MY&t=38s', 'Wf7bthXLvpA' , 'uhUEjnCC1pg' , 'wbJcJCkBcMg' ,'xvsgTVkvvg4' ,'XYaDAo9zdmE',
'Fb8j4kYZxK8' , 'nLB4YtsqyNU' , 'O1AeSzi8sns']

def fetch_video_views(video_ids):
    video_data = []
    for video_id in video_ids:
        url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=statistics&key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        views = data['items'][0]['statistics']['viewCount']
        video_data.append({'video_id': video_id, 'views': views})
    return video_data

if __name__ == "__main__":
    print(fetch_video_views(VIDEO_IDS))
