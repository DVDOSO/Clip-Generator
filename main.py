import SpeechToText, ClipEdit, Subtitles, pysrt, os, datetime
from moviepy import *

def deleteFile(delFile):
    if os.path.exists(delFile):
        os.remove(delFile)
    else:
        print("Error")

def generate(text):
    SpeechToText.textToMp3Short(text)

    i = 0
    for speech in os.listdir('./output'):
        Subtitles.genSubtitlesShort(f'./output/{speech}', i)
        i += 1
    
    i = 0
    for item in os.listdir('./output'):
        if(item[:6] == 'speech'):
            ClipEdit.createVideoShorts(f'./output/{item}', f'./output/output{item[6:-4]}.srt', i)
            i += 1

    for item in os.listdir('./output'):
        if(item[:6] == 'speech'):
            deleteFile(f'./output/{item}')
        if(item[:6] == 'output'):
            deleteFile(f'./output/{item}')
    deleteFile('speech.mp3')

generate("""
38/F I am celebrating Christmas with my mom 68/F, my brother 47/M and his family. My mom flew in from out of state and we are driving to a meetup location to spend time with my brother's family - a place in the mountains we all enjoy just for the holidays. All of us live hours away, our mom being the furthest, on the opposite coast. My brother and I are several hours away by car.

This year, we received the bad news that, while my mom has been at my place, her pipes froze and flooded her basement. She is upset, understandably, I helped her get everything started and have her insurance, a cleanup team and a general contractor all working on her place while she is with me. She then broached the topic that she wanted to extended her week stay to "two weeks or more". I said no, I need to get back to my regular routine and get ready to return to work. She's welcome to stay here as originally planned, which is until Saturday.

Then she said she may ask to ride back with my brother and his family to their home in another state (opposite direction than me). She refused to ask him until Christmas, so l gave my brother a heads up last night so he has a chance to speak with his wife. I also told him that he's under no obligation to say yes, as she is still welcome to stay with me until Saturday and her insurance company will be footing the bill for most of her stay at a hotel and meals (IF, BIG IF, her residence is uninhabitable, which we do not know at this time).

He told me he didn't have room to take her back with him (3 people in his car and no room for a 4th -assuming luggage is the issue). That I should let her stay with me because she's lonely. I told him I understood that, but I'm not wrong for wanting to cap my time with her at the one week originally planned. He had left that text on "send". My mom can be a challenging personality and with this unfortunate development, she's even more ... difficult. I love my mom, but I'm tired. I want my house back and don’t want to be criticized or complained at. I refused to allow my lonely mother to extend her stay with me, despite the recent damages to and unknown state of her home. AITAH for prioritizing my space and personal downtime over my mother's emotional needs?
""")