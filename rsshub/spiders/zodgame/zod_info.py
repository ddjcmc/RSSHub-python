# your cookie
cookie = ''

# your proxy
proxies =  {}

fid_model_dict = {3: 'I社前哨站', 119: '综合游戏资讯', 133: 'Room Girl', 127: '恋活！Sunshine', 99: 'AI少女', 106: 'Honey Select2', 98: '恋爱活动', 93: 'Play Home', 82: 'Honey Select', 97: '欲望工坊', 67: '人工学园2', 2: 'I社历代', 4: 'MOD&插件制作交流', 84: '故事创作及交流', 109: '求物及咨询区', 10: '3D动画&CG分享', 100: '日系3D游戏专区', 75: '3D定制女仆专区', 102: 'VAM 专区',
                 68: '欧美3D游戏专区', 132: 'Fallen Doll讨论区', 16: '大水吧', 17: '萌系文化胡侃室', 30: '萌绘部室', 18: '二次元贴图板', 11: 'GAL交流', 120: '手游交流', 13: '绅士游戏集散地', 25: 'CG同萌', 12: '萌你妹果园', 111: 'MMD专区', 96: ' Comic Market', 110: '裸奔求物公园', 104: '游戏广场', 36: '动漫园地', 27: '妄想心音', 122: '银发教会', 101: '靴下汉化组', 20: '招募启事', 21: '意见及申诉区', 19: '版主议会'}

def get_zod_space_url( pure_uid: str = '763195', page: int = 1):
        '''get space url'''
        print(f'uid={pure_uid} \tpage={page}')
        str_page = f'https://zodgame.xyz/home.php?mod=space&uid={pure_uid}&do=thread&view=me&type=thread&order=dateline&from=space&page={page}'
        str_nopage = f'https://zodgame.xyz/home.php?mod=space&uid={pure_uid}&do=thread&view=me&type=thread&from=space'
        return str_page if page > 1 else str_nopage


def get_zod_module_url(fid: int|str, page: int = 1):
        '''get module url'''
        str_nopage = f'https://zodgame.xyz/forum.php?mod=forumdisplay&fid={fid}&orderby=dateline&filter=author'
        str_page = f'https://zodgame.xyz/forum.php?mod=forumdisplay&fid={fid}&orderby=dateline&filter=author&page={page}'
        return str_page if page > 1 else str_nopage
