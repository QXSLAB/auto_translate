# coding=utf-8
from pynput import mouse,keyboard
# mouse.Button;
# mouse.Controller;

# keyboard.Key;
# keyboard.Controller;

# controller=mouse.Controller();

# # ��ȡ���λ��
# print(controller.position);

# # # ��λ
# controller.position=(0,20);

# # # �ƶ�
# controller.move(150,32)

# # �����Ҽ�
# controller.click(mouse.Button.right,1)

# # ˫�����
# controller.click(mouse.Button.left,2)

# # ��ס���
# controller.press(mouse.Button.left)
# # �ͷ����
# controller.release(mouse.Button.left)

# ������,�������¹�
# controller.scroll(0,-100);
def on_move(x,y):
    print(x,y)
def on_click(x,y,button,pressed):
    print(x,y)
def on_scroll(x,y,dx,dy):
    print(x,y)
# #�������
# with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
#     listener.join()

# ֹͣ����,�����ڻص��з���False
# mouse.Listener.stop()


# #�����Ǽ���
# #���Ƽ���
keyboardController=keyboard.Controller();
# ��ס�ո�
keyboardController.press(keyboard.Key.space);
# �ɿ��ո��
keyboardController.release(keyboard.Key.space);
# ��סa
keyboardController.press('a');
keyboardController.release('a');                 

                                                                                                                                                                                                                                               
def on_press(key):
    print(key);
def on_release(key):
    print(key);
# # �������̰���
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
# ֹͣ����,�����ڻص��з���False
# keyboard.Listener.stop()
 