import textstat

#taking a input paragraph
sentence = input("Enter a sentence: ")

#calculating number of words,sentences and syllables
word_count = textstat.lexicon_count(sentence)
sent_count = textstat.sentence_count(sentence)
syllable_count = textstat.syllable_count(sentence)

#calculating words per sentence Ratio
WordSentRatio = word_count/sent_count

#calculating Syllable per word Ratio
SyllableWordRatio = syllable_count/word_count

#calculating Flesch Kincaid Grade level
grade = (0.39 * WordSentRatio) + (11.8 * SyllableWordRatio) - 15.59

#calculating FLesch ease score
score = 206.835 - 1.015 * (WordSentRatio) - 84.6 * (SyllableWordRatio)

#printing Flesch Grade and Flesch Score
print("Flesch Kincaid Grade:",round(grade,2),"Flesch Ease Score:",round(score,2))

#rounding the grade and score to approximate integer values
grade = round(grade)
score = round(score)

#classifying sentences into different difficulty levels based on scores and grades
if 90 <= score <= 100:
  print("Level of Difficulty->Very easy to read")
  print("Rounded Grade is:",grade)
  print("Can be read by 5th grade students")
elif 80 <= score <= 90:
  print("Level of Difficulty->Easy to read")
  print("Rounded Grade is:",grade)
  print("Can be read by 6th grade students")
elif 70 <= score <= 80:
  print("Level of Difficulty->Fairly easy to read")
  print("Rounded Grade is:",grade)
  print("Can be read by 7th grade students")
elif 60 <= score <= 70:
  print("Level of Difficulty->Plain English")
  print("Rounded Grade is:",grade)
  print("Can be read by 8th and 9th grade students")
elif 50 <= score <= 60:
  print("Level of Difficulty->Fairly difficult to read")
  print("Rounded Grade is:",grade)
  if grade <= 10:
    print("Can be read by 10th,11th and 12th grade students")
  else:
    print("Can be read by College Students")
elif 30 <= score <= 50:
  print("Level of Difficulty->Difficult to read")
  print("Rounded Grade is:",grade)
  print("Can be read by College students")
elif 0 <= score <= 30:
  print("Level of Difficulty->Very difficult to read")
  print("Rounded Grade is:",grade)
  if grade < 16:
    print("Can be read by College students")
  else:
    print("Can be read by College Graduates")
elif score < 0:
  print("Level of Difficulty->Peak Difficulty level")
else:
  print("Level of Difficulty->Too easy to read.Even a small child can read it.")
  print("Rounded Grade is:",grade)
  print("Can be read by College Graduate")
print("Total words:",word_count)
print("Total Sentences:",sent_count)
print("Average Syllables per word:",round(SyllableWordRatio,2))
print("Average Words per Sentence:",round(WordSentRatio,2))
