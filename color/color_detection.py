import cv2
import pandas as pd


#declaring global variables (are used later on)
clicked = False
r = g = b = 0

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('color/colors.csv', names=index, header=None)


#function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


def rgb_name(dictionary_colors):
    for index in dictionary_colors.keys():
        colors = dictionary_colors[index]['color']
        r = colors[0]
        g = colors[1]
        b = colors[2]
        #Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        if 'brown' in text.lower():
            print('brown')
        if 'black' in text.lower():
            print('black')
        if 'white' in text.lower():
            print('white')
        if 'red' in text.lower():
            print('red')
        if 'yellow' in text.lower():
            print('yellow')
        if 'pink' in text.lower():
            print('pink')
        if 'blue' in text.lower():
            print('blue')
        if 'purple' in text.lower():
            print('purple')
        if 'grey' in text.lower():
            print('grey')
        if 'green' in text.lower():
            print('green')