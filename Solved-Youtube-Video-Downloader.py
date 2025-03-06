from yt_dlp import YoutubeDL



def download_video(url, save_path):
    
    
    try:    
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save path and filename
            'format': 'best',  # Download the best quality available
        }

    
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print('Video Downloaded Successfully!')
    

    except Exception as e:
        print(f"An error occurred: {e}")



# Example usage
url = 'https://youtu.be/IwjBJb4-hrc?si=WtlHaTwEpaih23Q0'

save_path = 'F:/Important Data'

download_video(url, save_path)







