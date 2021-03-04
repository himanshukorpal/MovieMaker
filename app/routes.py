from flask import render_template, url_for, request, redirect
from app import app
from app import db
from movie import VideoMaker

video_files= []
music_files = []
template = db.template
music = db.music
for temp in template.find():
    video_files.append(temp)

for temp in music.find():
    music_files.append(temp)

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/getstarted', methods=['GET','POST'])
def getstarted():
    if request.method == "POST":
        video_select = request.form.get('video-select')
        music_select = request.form.get('music-select')
        text_select = request.form.get('text-select')
        if None in [music_select, video_select] or text_select == '' :
                pass
        else:
            VideoMaker(video_select, music_select, text_select)
            return redirect(url_for('index'))



    return render_template('getstarted.html', video=video_files, music=music_files)

