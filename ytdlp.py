import yt_dlp

ydl_opts = {
    'cookies': '/path/to/cookies.txt',  # Çerez dosyanızın yolu
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['<video_url>'])  # İndirmek istediğiniz video URL'si
