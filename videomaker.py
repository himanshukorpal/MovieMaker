import numpy as np
# from config import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
# from transitions import vortex,arrive,vortexout,cascade


from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects


# helper function
rotMatrix = lambda a: np.array( [[np.cos(a),np.sin(a)], 
                                         [-np.sin(a),np.cos(a)]] )

def vortex(screenpos,i,nletters):
    d = lambda t : 1.0/(0.3+t**8) #damping
    a = i*np.pi/ nletters # angle of the movement
    v = rotMatrix(a).dot([-1,0])
    if i%2 : v[1] = -v[1]
    return lambda t: screenpos+400*d(t)*rotMatrix(0.5*d(t)*a).dot(v)
            
def cascade(screenpos,i,nletters):
    v = np.array([0,-1])
    d = lambda t : 1 if t<0 else abs(np.sinc(t)/(1+t**4))
    return lambda t: screenpos+v*400*d(t-0.15*i)

def arrive(screenpos,i,nletters):
    v = np.array([-1,0])
    d = lambda t : max(0, 3-3*t)
    return lambda t: screenpos-400*v*d(t-0.2*i)
    
def vortexout(screenpos,i,nletters):
    d = lambda t : max(0,t) #damping
    a = i*np.pi/ nletters # angle of the movement
    v = rotMatrix(a).dot([-1,0])
    if i%2 : v[1] = -v[1]
    return lambda t: screenpos+400*d(t-0.1*i)*rotMatrix(-0.2*d(t)*a).dot(v)





def maker(video_path, text, effect):
        video_clip = VideoFileClip(video_path)
        fps = video_clip.fps

# WE CREATE THE TEXT THAT IS GOING TO MOVE, WE CENTER IT.
        w ,h = video_clip.size
        screensize = video_clip.size
        txtClip = TextClip(text,color='white', font="Amiri-Bold",
                           kerning = 5, fontsize=100)
        cvc = CompositeVideoClip( [txtClip.set_position('center')
        ],size=screensize)

# THE NEXT FOUR FUNCTIONS DEFINE FOUR WAYS OF MOVING THE LETTERS



# WE USE THE PLUGIN findObjects TO LOCATE AND SEPARATE EACH LETTER

        letters = findObjects(cvc, rem_thr=0) # a list of ImageClips


# WE ANIMATE THE LETTERS

        def moveLetters(letters, funcpos):
            return [ letter.set_pos(funcpos(letter.screenpos,i,len(letters)))
                      for i,letter in enumerate(letters)]

# clips = [ CompositeVideoClip( moveLetters(letters,funcpos),
#                               size = screensize).subclip(0,5)
#           for funcpos in [vortex, cascade, arrive, vortexout] ]

# WE CONCATENATE EVERYTHING AND WRITE TO A FILE

        clips = CompositeVideoClip(moveLetters(letters, effect), size = screensize)
        clips = clips.set_duration(5)

        final_clip = CompositeVideoClip([video_clip, clips])

# final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile('../../coolTextEffects.avi',fps=25,codec='mpeg4')
