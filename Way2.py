'''This program dynamically takes input from user to filter
 the subjects according to given list of keywords one or more '''

keywords=input("enter keywords seperated by spaces: ").split()
subject_mails=input("enter subject mails seperated by comma: ").split(",")
# print(keywords) // to check the keywords
# print(subject_mails) // to print the mail subjects
keyword_lower=[]
for keyword in keywords:
    keyword_lower.append(keyword.lower())
# print(keyword_lower) // to print the lower_keywords


def filter_mails(keywords,subject_mails):
    filtered_mails=[]
    for subject in subject_mails:
        if any(keyword in subject.lower() for keyword in keyword_lower):
            filtered_mails.append(subject)
    return filtered_mails

result=filter_mails(keywords,subject_mails)
print(result)