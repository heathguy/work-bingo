# Work Bingo
# Generate X number of pdf bingo cards based on options for each space
#
import os
import sys
from fpdf import FPDF
from random import randint

if len(sys.argv) < 2:
	print "Error: Missing number of cards to print."
	print "Usage: 'python bingo-card-generator.py <number of cards to generate>'"
	print "Ex: 'python bingo-card-generator.py 5'"
	exit()
else:
	numCardsToGenerate = sys.argv[1]
	print "GENERATING " + str(numCardsToGenerate) + " CARD(S)"

options = []
options.append("Free Space")
#MB Options
options.append("MB says 'Mumbo Jumbo'")
options.append("MB says 'Wooo Weee'")
options.append("MB sings")
options.append("MB says 'Were in the Home Stretch'")
options.append("MB says 'Just Send It'")
options.append("MB says 'I just sell food'")
#JC Options
options.append("JC says 'We got a Situation'")
options.append("JC says 'Come on People'")
options.append("JC says 'This is all Buttercup'")
options.append("JC says 'What Bus, What Dent'")
options.append("JC says 'Too Bad!'")
#KS Options
options.append("KS calls someone Babe/Bub")
options.append("KS talks about the weather")
options.append("KS talks about the traffic")
options.append("KS yells at Customer Service")
#RJ Options
options.append("RJ says 'Alright'")
#MV Options
options.append("MV 'Calls for da Order'")
#MRM Options
options.append("MRM yells from his office")
options.append("MRM gives a Dress Down Day")
options.append("MRM plays music")
options.append("MRM calls the office")
#IT Options
options.append("Email is Down")
options.append("Phones are Down")
options.append("Internet is not Working")
#Warehouse Options
options.append("Warehouse cannot find a Product")
#Office Options
options.append("Fryer Oil is Changed")
options.append("By Car Order is Called In")
options.append("Call for Child Support")
options.append("Invoice Printer runs out of Paper")
options.append("Any sales rep complains we are out of a product")
options.append("Someone tries to talk to Jill while she is on the phone")
options.append("Someone mentions a past employee")

#print options
numOptions = len(options)-1
#print "NUMBER OPTIONS: "+str(numOptions)
card = []
usedNumbers = []
cardNum = 1
for i in range(25): # 25 boxes on a card
	#print "i: "+str(i)
	if i == 12:
		card.append(options[0])
		usedNumbers.append(i)
	else:
		randomOptionNum = randint(1,numOptions)
		while randomOptionNum in usedNumbers:
			randomOptionNum = randint(1,numOptions)
		usedNumbers.append(randomOptionNum)
		#print "RANDOM OPTION NUMBER: "+str(randomOptionNum)
		randomOption = options[randomOptionNum]
		#print "RANDOM OPTION: "+randomOption
		card.append(randomOption)

for c in range(int(numCardsToGenerate)):
	pdf = FPDF()
	pdf.add_page()

	# Write Title on Page
	pdf.set_font('arial', 'B', 22.0)
	pdf.set_xy(0, 35)
	pdf.set_text_color(255,0,0)
	pdf.cell(0,0,"Work Bingo",0,0,'C',False,'')
	pdf.set_text_color(0,0,0)

	#Build the board
	boxNum = 1
	x1cord = 30.0
	y1cord = 50.0
	x2cord = 60.0
	y2cord = 80.0
	usedNumbers = []
	for b in range(25):
		bname1 = "box"+str(b)
		bname2 = "box"+str(b)+"_text"
		#Draw the Box
		pdf.set_line_width(0.5)
		pdf.rect(x1cord, y1cord, 30.0, 30.0)
		#Add the text
		if b == 12: #Print the logo
			#pdf.set_xy(x1cord+5, y1cord+5)
			pdf.image('./logo.jpg',x1cord+2,y1cord+5,26,21)
			usedNumbers.append(b)
		else:
			pdf.set_font('arial', '', 10.0)
			pdf.set_xy(x1cord, y1cord+5)
			#pdf.cell(ln=0, h=2.0, align='C', w=10.0, txt=card[b], border=0)
			#pdf.multi_cell(w: 30.0, h: 2.0, txt: card[b], border: 0, align: str = 'C', fill: bool = False)
			randomOptionNum = randint(1,numOptions)
			while randomOptionNum in usedNumbers:
				randomOptionNum = randint(1,numOptions)
			usedNumbers.append(randomOptionNum)
			#print "RANDOM OPTION NUMBER: "+str(randomOptionNum)
			randomOption = options[randomOptionNum]
			pdf.multi_cell(30.0, 5.0, randomOption, 0, 'C', False)
			#pdf.multi_cell(30.0, 5.0, card[b], 0, 'C', False)
		x1cord += 30
		x2cord += 30
		if (boxNum % 5) == 0: #if row chages reset x cords drop the y cords
			x1cord = 30.0
			x2cord = 60.0
			y1cord += 30.0
			y2cord += 30.0
		boxNum += 1
		
	#print elements

	pdfTitle = "Work Bingo Card"
	#f = Template(format="Letter", elements=elements, title=pdfTitle)

	#f.add_page()

	#and now we render the page
	fileName = "./work_bingo_card_" + str(cardNum) + ".pdf"
	pdf.output(fileName, 'F')
	cardNum += 1
