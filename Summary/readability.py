import textstat
import text_parser
text=text_parser.text
readability_index=textstat.flesch_reading_ease(text)
# print("The readability index of the following text:-\n",text," is \n",readability_index)