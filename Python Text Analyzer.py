# This is a Text Analyzer Program Built Using Python...

class Text_Analyzer(object):

    def __init__(self,Text):

        # Remove Punctuations: . ! , ?," (Repace with a space)
        Formatted_Text=Text.replace(".","").replace("!","").replace(",","").replace("?","").replace('"',"").replace("'","")

        # Convert into a Lower Case Text
        Formatted_Text=Formatted_Text.lower()
        self.FmtTxt=Formatted_Text

    def Frequency_Of_All_Unique_Words(self):

        # split text into words
         Word_List=self.FmtTxt.split(" ")

        # Create a Dictionary to store the frequency of all unique words
         WordFrequencyDict={}

        # Update the "WordFrequencyDict" dictionary by converting the "Word_List" list into a set and then count the unique words.
         for Word in set(Word_List):
             WordFrequencyDict[Word]=Word_List.count(Word)
         return WordFrequencyDict
    
    def Frequency_Of_A_Specific_Word(self,Word):

        # count the frequency of a specific word
        SpecificWordDict=self.Frequency_Of_All_Unique_Words()
        if Word in SpecificWordDict:
            return SpecificWordDict[Word]
        else:
            return 0

#Welcome Text
print("Hello...This is a Text Analyzer Program Built Using Python...")
print(" ")

# Collect User Input
UserInput=input("Type or Copy-Paste Your Paragraph Here : ")
print(" ")

# Call the Functuions
TextString1=Text_Analyzer(UserInput)
print("Your Text : ",UserInput)
print(" ")
print("Formatted Text :",TextString1.FmtTxt )
print(" ")
WordFrequencyDict=TextString1.Frequency_Of_All_Unique_Words()
print(WordFrequencyDict)
print(" ")
Word=input("Type a word for counts the frequency of that word : ")
print(" ")
Frequency=TextString1.Frequency_Of_A_Specific_Word(Word)
print("The Word","'",Word,"'","appears",Frequency,"times.")
print(" ")
print(" Saviska Jayawickrama - 2024 ")
print(" ")
