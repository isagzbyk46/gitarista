import yt_dlp

ydl_opts = {
    'cookies': 'cookies/cookies.txt',  # Repository içindeki çerez dosyasının yolu
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['<video_url>'])  # İndirmek istediğiniz video URL'si
