
from xml.etree import ElementTree	#needed for reading the xml doc
import csv							#needed for generating a csv file
import os
import glob							#needed for iterating through a directory


folder = 'testfiles/'  
f = open('test.csv','wb')

csvConverter = csv.writer(open('test.csv','wb'), delimiter= ',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
csvConverter.writerow( ["Title"] +["Keywords"] + ["Authors"] + [ "Contact Name"] + ["Publication Date"] + ["Abstract"] + ["Methods"]  )

#Big loop that iterates through all files in the specified folder
for infile in glob.glob (os.path.join(folder, '*.*') ): 
	print "current file is: " + infile


	#opens a single document & parses out tree structure
	with open(infile, 'rt') as f:
		tree = ElementTree.parse(f)
		

	#TITLE locates a node by the path
	titleList = []
	for path in [ './dataset/title' ]:
		title = tree.find(path)
		titleList.append(title.text)
	
	#KEYWORDS Creates an empty list to hold keywords
	keywordList = []
	for keyword in tree.iter('keyword'):
		keywordList.append(keyword.text)
	
	#AUTHORS Adds authors to an authorList
	authorList = []
	for creator in tree.iter('creator'):
		for individualName in creator.iter('individualName'):
			for givenName in individualName.iter('givenName'): 
				firstName = givenName.text
			for surName in individualName.iter('surName'):
				lastName =  surName.text
			authorList.append(lastName + ', ' + firstName)
	
	#CONTACTS Adds contacts to contactList
	contactList = []
	for contact in tree.iter('contact'):
		for individualName in creator.iter('individualName'):
			for givenName in individualName.iter('givenName'): 
				firstName = givenName.text
			for surName in individualName.iter('surName'):
				lastName =  surName.text
			contactList.append(lastName + ', ' + firstName)
	
	#ASSOCIATED PARTIES Adds associated parties to the author list
	for associatedParty in tree.iter('associatedParty'):
		for individualName in associatedParty.iter('individualName'):
			for givenName in individualName.iter('givenName'): 
				firstName = givenName.text
			for surName in individualName.iter('surName'):
				lastName =  surName.text
			authorList.append(lastName + ', ' + firstName)

	#PUBLICATION DATE Adds a publication date to a publication date list
	pubDateList = []			
	for pubDate in tree.iter('pubDate'):	
		pubDateList.append(pubDate.text)

	#ABSTRACT Adds abstract to the abstract list
	for abstract in tree.iter('abstract'):
		for para in abstract.iter('para'):
			for literalLayout in para.iter('literalLayout'): 
				abstract = literalLayout.text

	#METHODS Adds dataset methods to the dataset list
	for methods in tree.iter('methods'):
		for methodStep in methods.iter('methodStep'):
			for description in methodStep.iter('description'):
				for section in description.iter('section'):
					for para in section.iter('para'):
						for literalLayout in para.iter('literalLayout'):
							methodsDescription = literalLayout.text
							
				
	csvConverter.writerow([titleList] +[keywordList]+[authorList] + [contactList] + [pubDateList] + [abstract] + [methodsDescription])
	



# EXTRA CODE STUFFS		
#	associatedPartyTerm = tree.find('./dataset/associatedParty/individualName')
#	associatedParty = []	
#	if associatedPartyTerm is not None:
#		for node in tree.iter('associatedParty'):
#			for path in ['./dataset/associatedParty/individualName/givenName']:
#				node = tree.find(path)
#			for path in ['./dataset/associatedParty/individualName/surName']:
#				lastName = tree.find(path)
#		associatedParty.append(lastName.text + ',' + node.text)
#	else: 
#		print "nope"
	
#	print associatedParty
#Opens a csv file named test.csv and writes rows to it. 
#adds a row to the csv file
#	csvConverter.writerow(['file'] + ['author']+ ['title'] + ['publication'] + ['abstract'] + ['journal name'] + ['publisher'] + ['peer reviewed']+['keywords'], )

#			for path in [ './dataset/creator/individualName/givenName']: 
#				name = tree.find(path)
#				print 'node.text' , name.text
#		for path in ['./dataset/creator/individualName/surName']:
#			lastName = tree.find(path)

#		authorList.append(lastName.text + ',' + node.text)
	
