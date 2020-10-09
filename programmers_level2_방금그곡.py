  
#테스트 케이스 26,27,28,30을 통과하지 못함 
def solution(m, musicinfos):
    new_musicinfos = []
    for musicinfo in musicinfos:
        musicinfo=musicinfo.split(',')
        length = ((int(musicinfo[1].split(':')[0])-int(musicinfo[0].split(':')[0]))*60) + ((int(musicinfo[1].split(':')[1])-int(musicinfo[0].split(':')[1])))
        title =musicinfo[2]
        sheet = (musicinfo[-1])*length

    # if m in sheet:
    #     new_musicinfos.append((length, title))
    
        while len(sheet) > len(m):
            if sheet.find(m) != -1:
                m_length = len(m)
                if sheet[sheet.find(m)+m_length:sheet.find(m)+m_length+1] == '#':
                    sheet = sheet[sheet.find(m)+m_length+2:]
                else:
                    new_musicinfos.append((length, title))
                    break
            else:
                break

    new_musicinfos=sorted(new_musicinfos, key=lambda x:x[0])
    if len(new_musicinfos) == 0:
        return "(None)"
    else:
        return (new_musicinfos[-1][-1])



#https://eda-ai-lab.tistory.com/506
# 몇 가지 간과한 점들
# 시간, 정렬, 멜로디 하나당 1분이란 사실


def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_ 


def caltime(music_):
    starttime=music_[0]
    endtime=music_[1]
    hour = 1 * (int(endtime.split(':')[0]) - int(starttime.split(':')[0]))
    if hour == 0:
        length = ((int(endtime.split(':')[1])-int(starttime.split(':')[1])))
    else:
        length = (hour*60) + ((int(endtime.split(':')[1])-int(starttime.split(':')[1])))
    return length

# from datetime import datetime
def solution(m, musicinfos):
    new_musicinfos = []
    for idx,musicinfo in enumerate(musicinfos):
        m=changecode(m)
        musicinfo = changecode(musicinfo)
        musicinfo=musicinfo.split(',')
        title =musicinfo[2]
        sheet = musicinfo[-1]
        length = caltime(musicinfo)
        print(length)
        if length<len(sheet):
            sheet = sheet[:length]
        elif length>len(sheet):
            mok=length//len(sheet)
            namuji = length%len(sheet)
            sheet = ((sheet)*mok)+sheet[:namuji]       
        else:
            sheet = sheet
        print(sheet)

        if m in sheet:
            new_musicinfos.append([idx,length, title])
        

    new_musicinfos=sorted(new_musicinfos, key=lambda x:(-x[1],x[0]))
    print(new_musicinfos)
    if len(new_musicinfos) == 0:
        return "(None)"
    else:
        return (new_musicinfos[0][2])
