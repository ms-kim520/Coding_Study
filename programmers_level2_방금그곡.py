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
