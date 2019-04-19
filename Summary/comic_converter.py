from PIL import Image,ImageDraw,ImageFont
import tkinter
from tkinter import filedialog
import textwrap

#created python files#
import summarizer
import readability
import text_parser
import sentiment
#created python files#


#function definition#

def textdraw(text,number):
	
	imageDrawList[k].text(((width-w/50)/50,(height+((height//10)-h)/2)),text,font=font,fill='black')
		

def getFinalString(text):
	newline=""
	
	newline+=textwrap.fill(text,width=50)
	newline+="\n"
	return newline

def getStringOutOfList(listName):
	return '\n'.join(listName)
		
def index_rating(index): 
    if index < 29:
    	return "Very Confusing"

    if index >= 29 and index < 49:
    	return "Difficult"

    if index >= 49 and index < 59:
    	return "Fairly Difficult"

    if index >= 60 and index < 69:
    	return "Standard"    	

    if index >= 70 and index < 79:
    	return "Fairly Easy"    	

    if index >= 80 and index < 89:
    	return "Easy"    	

    if index >=89:
    	return "Very Easy"

tkinter.Tk().withdraw()


caption = summarizer.final


img=Image.open('Pictures/Tulips.jpg')
width,height=img.size


novo = textwrap.wrap(caption, width=50,placeholder="",break_long_words="True")

finalStrings=[]
strList=[]

i=7
j=0
while i<=len(novo):
	if i % 8 == 0:
		finalStrings=novo[j:i]
		strList.append(finalStrings)
		j+=8
	i+=1

imageList=[]
i=0
while i<len(strList):
	imageList.append(Image.new('RGBA',(width+100,height+(height//2)),'white'))
	i+=1



iterVar=0
while iterVar<len(imageList):
	imageList[iterVar].paste(img,(5,5,(width+5),(height+5)))
	iterVar+=1



font=ImageFont.truetype('Font/digital-7.ttf',40)
w,h=font.getsize(caption)




imageDrawList=[]
imageIteration=0
while imageIteration<len(strList):
	imageDrawList.append(ImageDraw.Draw(imageList[imageIteration]))
	imageIteration+=1

k=0
while k<len(strList):
	textdraw(getStringOutOfList(strList[k]),k)
	k+=1
print("Number of pages ",len(strList))
# print("Readability index of the story is ",readability.readability_index)
print("-----Sentiment of the text is----- \n")
positive=sentiment.print_sentiment_scores(text_parser.text)['pos']*100
negative=sentiment.print_sentiment_scores(text_parser.text)['neg']*100

print("Positivity of the story is ",positive,"%")
print("Negativity of the story is ",negative,"%")
print("Story would be  ",index_rating(readability.readability_index)," to comprehend")
print("Our rating is ",(positive+(100-negative)+readability.readability_index)/3,"%")

print("Images stored in Pics")
displayVar=0
while displayVar<len(imageList):
	imageList[displayVar].save('Pics/Image'+str(displayVar)+'.png')
	displayVar+=1