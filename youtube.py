from googleapiclient.discovery import build
  
api_key = 'AIzaSyBy4qJESV2vU_7d-EmOvB70WdkJOm6QFd8'
  
def video_comments(video_id):
  
    youtube = build('youtube', 'v3', developerKey=api_key)
  
    video_response=youtube.commentThreads().list(
    part='snippet,replies',
    videoId=video_id,
    maxResults=25
    ).execute()

    comments = []

    while video_response:
        
        for item in video_response['items']:
            
            if len(comments)<=20:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
                print(comment)
            else:
                break
                
        break
        # if 'nextPageToken' in video_response:
        #     video_response = youtube.commentThreads().list(
        #             part = 'snippet,replies',
        #             videoId = video_id,
        #             maxResults=20
        #         ).execute()
        # else:
        #     break
    print(len(comments))
    return comments
  

video_id = "Z1RJmh_OqeA" # add video id received from form

# cc = video_comments(video_id)