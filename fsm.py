#coding=utf-8
from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_azurlane(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '碧藍航線' in text.lower()
        return False

    def is_going_to_whiteeagle(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '白鷹' in text.lower()
        return False

    def is_going_to_eagle(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '企業' in text.lower()
        return False

    def is_going_to_esex(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '艾賽克斯' in text.lower()
        return False

    def is_going_to_royal(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '皇家' in text.lower()
        return False

    def is_going_to_opai(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '貝爾法斯特' in text.lower()
        return False

    def is_going_to_sakura(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '重櫻' in text.lower()
        return False

    def is_going_to_loli(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '長門' in text.lower()
        return False

    def is_going_to_ironblood(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '鐵血' in text.lower()
        return False

    def is_going_to_hinnyuu(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '希佩爾' in text.lower()
        return False

    def is_going_to_eastempire(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '東煌' in text.lower()
        return False

    def is_going_to_sister(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '逸仙' in text.lower()
        return False

    def is_going_to_freedom(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '自由鳶尾' in text.lower()
        return False

    def is_going_to_triumph(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '凱旋' in text.lower()
        return False

    def is_going_to_holysee(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '維希教廷' in text.lower()
        return False

    def is_going_to_thigh(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '讓巴爾' in text.lower()
        return False

    def is_going_to_northunion(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '北方聯合' in text.lower()
        return False

    def is_going_to_abpopa(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '阿芙樂爾' in text.lower()
        return False

    def on_enter_azurlane(self, event):
        sender_id = event['sender']['id']
        responese = send_image_message(sender_id, "https://i.imgur.com/hi2J6zS.jpg")
        responese = send_text_message(sender_id,"碧藍航線\nhttp://www.azurlane.jp")
        responese = send_text_message(sender_id, "azurlane，碧藍航線\r\n關於碧藍航線的一些角色們\r輸入 白鷹 皇家 重櫻 鐵血 東煌 自由鳶尾 維希教廷 北方聯合等陣營名稱來查看\n輸入碧藍航線來回到這個頁面")

    def on_enter_whiteeagle(self, event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"白鷹\n")
        send_text_message(sender_id, "崇尚自由與科技的大國，將主要的發展重心放在了航空技術之上\n式目前時裝艦娘數量最多的陣營\n\n角色介紹輸入: 企業 艾賽克斯")
    
    def on_enter_eagle(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/S2z5yt5.jpg")
        send_text_message(sender_id, "主技能：空中支援時，有40%（70%）機率造成兩倍傷害，並使自身進入隱身狀態迴避所有傷害，持續8秒\n建造時間：4小時20分")
    def on_enter_esex(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/CFd8PMS.jpg")
        send_text_message(sender_id, "善战之舰：自身发动空袭时，额外使用TBF复仇者编队进行一顿攻击Lv.1（Lv.10），该编队的鱼雷将对命中的敌方造成进水持续伤害（伤害依据航空属性和技能等级）；自身对战列舰（不包括战巡、航战）伤害提高4.0%（10.0%）\n航空列阵:出击时，队伍中每有一个白鹰联邦航母或轻航角色，自身航空、防空提升1.5%（5.0%）；自身舰载机击落敌方飞机时，自身航空提高1.0%（3.0%）（该效果最高叠加5层）。\n绝对回避：出击时，若队伍中至少有4名白鹰角色，则全队成员受到的航空鱼雷或轰炸攻击时，有4.5%（12.0%）的概率将此次伤害降低至1。\n建造時間：4小時25分")

    def on_enter_royal(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"皇家\n")
        send_text_message(sender_id, "歷史悠久的皇權式國家，擁有最悠久的造船歷史與艦船性能平衡\n完加長提到的皇家隊，指的是以伊莉莎白女王為中心組隊伍。\n\n角色介紹輸入: 貝爾法斯特")
    
    def on_enter_opai(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "http://i.imgur.com/XFqag0R.jpg")
        send_text_message(sender_id, "主技能：戰鬥開始10秒後使用煙霧彈，隨後每20秒有20%機率使用煙霧彈，處於煙幕中的先鋒部隊迴避率提高15%(35%)，受到航空傷害降低15%(35%)，持續10秒，同技能效果不疊加。\n建造時間：1小時25分")

    def on_enter_sakura(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"重櫻\n")
        send_text_message(sender_id, "神祕的東方皇權式國家，世人對之知之甚少，其艦船擅長魚雷戰。\n在本作中最大的特點是重櫻艦娘幾乎都帶有獸耳和尾巴屬性，為目前遊戲中的敵艦擔當\n\n角色介紹輸入：長門")
    
    def on_enter_loli(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id, "https://i.imgur.com/X4xCzkG.jpg")
        send_text_message(sender_id, "主技能：作為旗艦出擊时，隊伍中的重樱艦娘炮擊提高4.0%（10.0%），裝填、命中提高5.0%（20.0%），重樱航母造成的傷害提高5.0%（20.0%）\nBIG SEVEN-樱：主炮開火時，有20.0%（40%）的概率朝自己前方直線發射一輪專屬彈幕(依據技能等级)\n建造時間：4小時20分")

    def on_enter_ironblood(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"鐵血\n")
        send_text_message(sender_id, "強硬軍事化的獨裁國家，叛變了「碧藍航線」。\n其艦船大體防禦優秀，且特點是艦首是鯊魚型的，顯示了鐵血的侵略性。\n角色詳細輸入: 希佩爾")

    def on_enter_hinnyuu(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://i.imgur.com/MVdvpjH.jpg")
        send_text_message(sender_id, "守衛之盾:每隔30秒。生成2面旋轉的護盾，每个護盾阻擋10發子彈，護盾持续5（15）秒\n建造時間：2小時")

    def on_enter_eastempire(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"東煌\n")
        send_text_message(sender_id, "文化燦爛的文明古國，由於歷史原因軍事實力在「碧藍航線」中處於弱勢。\n然而在之後實裝的新船給東煌增加了很大的戰力。她們分別是鞍山、撫順、長春、太原。\n角色詳細輸入: 逸仙")

    def on_enter_sister(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://i.imgur.com/ZJ4lLES.jpg")
        send_text_message(sender_id, "與寧海、平海同時出擊時，隊伍中逸仙、寧海、平海受到傷害降低8.0%(滿级20.0%)，迴避率提高15.0%(滿级30.0%)。\n建造時間：40分")

    def on_enter_freedom(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"自由鳶尾\n")
        send_text_message(sender_id, "為復國而從維希教廷中獨立出來的新勢力，加入碧藍航線並與皇家和白鷹聯合作戰。\n最早只有路易九世一條方案艦，2018年7月的活動中實裝了不少該陣營新船。\n角色詳細輸入: 凱旋")

    def on_enter_triumph(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://i.imgur.com/hH82iVQ.jpg")
        send_text_message(sender_id, "鳶尾之光：主炮連續命中同一目標時（同一子彈命中複數目標時，均可作為判定對象），提升自身裝填屬性20%（40%），最高疊加4層，每秒最多觸發一次，裝填提升效果生效期間，若命中非判定目標，則生效層數清零\n攻防轉換：裝備作為先鋒領艦出擊時，主炮效率提高5.0%（20%），防空炮效率降低30%。\n建造時間：無法建造")

    def on_enter_holysee(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"維希教廷\n")
        send_text_message(sender_id, "憑藉信仰統治的教會國家，造船技術原本僅次於皇家。現處在被鐵血與塞壬侵略和被皇家與白鷹圍剿的夾縫中苟延殘喘地生存。\n2018年7月活動中新增的陣營。 \n角色詳細輸入: 讓巴爾")

    def on_enter_thigh(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://i.imgur.com/tZzk9Xb.jpg")
        send_text_message(sender_id, "海盜之魂：每次進行炮擊的第一輪跨射傷害提高40.0%（60.0%）；手動進行瞄準時，手動發射帶來的跨射傷害增幅效果提高到40.0%（60.0%）\n最後的炮火：裝備【四聯裝380mm主炮Mle1935】主炮時，主炮的暴擊率提高10.0%（30.0%），主炮暴擊造成的傷害提高20.0%（50.0%）\n建造時間：5小時50分")

    def on_enter_northunion(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,"北方聯合\n")
        send_text_message(sender_id, "官方沒有給出任何說明，目前暫時只有阿芙樂爾一條船。在一週年慶典前為開荒證明，沒有在開服時就遊玩的玩家無法獲得阿芙。\n不過在一周年慶典中又可以限時獲得了。\n2018年7月活動中新增的陣營。 \n角色詳細輸入: 阿芙樂爾")

    def on_enter_abpopa(self, event):
        sender_id = event['sender']['id']
        send_image_message(sender_id,"http://i.imgur.com/nmYk54l.jpg")
        send_text_message(sender_id, "改變时代的炮聲：全體先锋部隊造成傷害提高15.0%（35.0%）\n建造時間：無法建造")




