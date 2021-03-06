from flask import render_template, url_for, request, redirect, flash, session
from app import app
from app import db
from videomaker import maker, vortex,cascade,arrive,vortexout

# from transitions import vortex,cascade,arrive,vortexout

video_files= []
music_files = []
template = db.template
music = db.music
for temp in template.find():
    video_files.append(temp)

for temp in music.find():
    music_files.append(temp)

transitions = {'vortex':vortex, 'cascade': cascade, 'arrive' : arrive, 'vortexout' : vortexout}

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/getstarted', methods=['GET','POST'])
def getstarted():
    if request.method == "POST":
        video_select = request.form.get('video-select')
        music_select = request.form.get('music-select')
        effect_select = request.form.get('effect-select')
        text_select = request.form.get('text-select')
        if None in [music_select, video_select, effect_select] or text_select == '' :
            flash("You Are Misssing Some Fields to Select or Fill", "warning")
            return redirect(url_for('getstarted'))

        else:
            maker(video_select, text_select, transitions[effect_select], music_select)
            flash("", "show")
            # return redirect(url_for('getstarted'))



    return render_template('getstarted.html', video=video_files, music=music_files, transitions=transitions)

