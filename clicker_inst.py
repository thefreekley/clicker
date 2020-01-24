import pyautogui
import time
import random
import win32gui
import pyperclip

subs=0
mean = 0

b_left=[617,52]
b_like1=[700,480]
b_like2=[954,480]
b_sub=[800,140]
b_ak=[100,150]
b_like=624 #кордина у для іконкі лайка
b_koment=[727,1000]
b_public=[1230,1000]
b_komentI=666 #кордина х іконкі комента
coment_emodzi=[
    "😀","😁","😂","😃","😄","😉","😊","😌","☄",
    "😍","😎","😗","😙","😟","😣","😨","✨","💫",
    "😬","😮","😯","😱","😲","😳","🙀","🧚","⭐",
    "🙈","🙉","🙊","😸","😺","😻","😼","🤩","‍🌟",
    "😽","🙀","💯","💥","💦","💣","💡","🔥","🌈"]
coment_text=[
    ")","))0","))","o)0",")0","неплохо",
    "оу)","*)","omg)0","харош","(0_0)",
    "??!)","даже так","Ао)","познавательно",
    "воу"
]

times = 0.5

def introduction():
    for i in range(1, 5):
        time.sleep(1)
        print("it starts over " + str(i) + " seconds")
    print("I`m begin")

def x(inf):
    return int(inf)

def y(inf):
    return int(inf)

def back_of():
    if check(616, 52)==(38, 38, 38):
        pyautogui.click(x(b_left[0]), y(b_left[1]), duration=times)
    else:
        time.sleep(2)
        pyautogui.click(x(b_left[0]), y(b_left[1]), duration=times)

print("AUTO INST CLICKER")
print("*****************")
Mod=input("cheat - 1 || come-off - 2 \n")
if Mod=="1":
    flag = input("How much are subscriber in this person? \n")  # 16448250
    AviableComent = input("With coment?\n")
    if AviableComent == "yes" or AviableComent == "with":
        AviableTextInComent = input("Coment with text?\n")
    AviableSubscription = input("With subscription?\n")


    def coment_():
        cos = ""
        yea = random.randint(1, 4)
        for i in range(0, yea):
            cos += coment_emodzi[random.randint(0, coment_emodzi.__len__()) - 1]

        # print(coment_emodzi.__len__())
        if AviableTextInComent.lower() == "yes" or AviableTextInComent.lower() == "with":
            if (random.randint(0, 3) == 2):
                cos += coment_emodzi[random.randint(0, coment_text.__len__())]
        return cos






    introduction()
    # кароч для комента середня по х буде 473
    # а по у 127 пікселів і функція яка перевіряє де знак комента:

    def check(i_x, i_y):
        i_desktop_window_id = win32gui.GetDesktopWindow()
        i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
        long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
        i_colour = int(long_colour)
        return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


    def coment():
        pyautogui.scroll(-360, 0, 1000)
        time.sleep(0.5)
        for i in range(1, 50):
            if check(b_like, 172 + i * 15) == (237, 73, 86):  # 172 + i * 15

                value_coment=coment_();
                pyperclip.copy(value_coment)
                pyautogui.click(b_komentI, 172 + i * 15, duration=times)
                pyautogui.doubleClick(x(b_koment[0]), y(b_koment[1]), duration=times)
                #time.sleep(0.5)
                pyautogui.keyDown('ctrl')
                pyautogui.press('v')
                pyautogui.keyUp('ctrl')

                time.sleep(0.5)
                pyautogui.click(x(b_public[0]), y(b_public[1]), duration=times)
                back_of()

#616 52


    def cruel(x3, y3, bila,num_of):
        global subs
        global mean
        # condition=win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), int(x(x3)),int(y(y3)))
        pyautogui.moveTo(x(x3), y(y3), duration=times)
        if check(x(x3), y(y3)) == (255, 255, 255):
            print("place is void")
        else:
            mean = mean+1
            print(str(num_of+1)+".check out.... sub:" + str(subs) + " likes:" + str(mean) + " <^=" + str(win32gui.GetCursorPos()))
            pyautogui.click(x(x3), y(y3), duration=times / 5)  # x=514 y=542"," 774","1000
            pyautogui.doubleClick(x(960), y(350), duration=times)
            pyautogui.doubleClick(x(960), y(350), duration=times/5)
            if AviableComent.lower() == "yes" or AviableComent.lower() == "with":
                if bila == 0:
                    coment()
            back_of()

    init_bre=0
    for i in range(0, int(flag)+init_bre):
        pyautogui.click(x(b_ak[0]), y(b_ak[1]), duration=times)
        time.sleep(3)
        # color=win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), int(x(422)),int(y(550)))
        # print(color)
        #print(check(x(619), y(143)))

        if check(x(b_like1[0]), y(b_like1[1])) == (250, 250, 250):
            print("this ak haven`t any photo or is closed")
            print("leaft...")
            init_bre+=1
        else:
            subs+=1
            cruel(b_like1[0], b_like1[1], 0,i)
            cruel(b_like2[0], b_like2[1], 1,i)
            # cruel(1000,542)

        if AviableSubscription == "yes" or AviableSubscription == "with":
            if check(x(b_like1[0]), y(b_like1[1])) != (250, 250, 250) and check(x(b_sub[0]), y(b_sub[1])) != (
            255, 255, 255):
                color_of_1 = check(int(x(b_like1[0])), int(y(b_like1[1])))
                pyautogui.click(x(b_sub[0]), y(b_sub[1]), duration=times)
                color_of_2 = check(int(x(b_like1[0])), int(y(b_like1[1])))
                time.sleep(1)
                if color_of_1 != color_of_2:
                    pyautogui.scroll(-360, 0, 1000)

        back_of()
        pyautogui.moveTo(x(428), y(161), duration=times)
        pyautogui.scroll(-80, 0, 1000)



else:
    times=0.5
    general=input("How much i must come-of from your subscribers\n")
    introduction()
    for i in range(0,int(general)):
        pyautogui.click(x(1840), y(300), duration=times)
        pyautogui.click(x(959), y(923), duration=times)
        pyautogui.moveTo(x(959), y(923), duration=times)
        pyautogui.scroll(-70, 0, 1000)



