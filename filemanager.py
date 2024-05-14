import os
import shutil

main_file = "filemanager.py"
# directory paths
source = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard"

audio_folder = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\audio"

images_folder = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\images"

programming_folder = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\programming"

text_folder = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\text"

video_folder = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\video"

pdf_folder = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\pdf"

document_folder = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document"

maths_folder_audio = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\audio\math"

history_folder_audio = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\audio\history"

science_folder_audio = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\audio\science"

computer_folder_audio = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\audio\computer"

maths_folder_images = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\math"

science_folder_images = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\science"

history_folder_images = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\history"

computer_folder_images = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\computer"

maths_folder_document = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\math"

science_folder_document = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\science"

history_folder_document = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\history"

computer_folder_document = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\document\computer"

computer_folder_pdf = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\pdf\computer"

history_folder_pdf = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\pdf\history"

science_folder_pdf = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\pdf\science"

maths_folder_pdf = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\pdf\math"

maths_folder_programming = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\programming\math"

science_folder_programming = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\programming\science"

history_folder_programming = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\programming\history"

computer_folder_programming = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\programming\computer"

computer_folder_video = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\video\computer"

history_folder_video = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\video\history"

science_folder_video = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\video\science"

maths_folder_video = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\video\math"

maths_folder_text = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\text\math"

science_folder_text = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\text\science"

computer_folder_text = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\text\computer"

history_folder_text = r"C:\Users\azeem\OneDrive\Desktop\pdfwizard\text\history"

files = os.listdir(source)

#print(files)
# file formats list
audio_file_formats = ['mp3', 'wav']
doc_file_formats = ['doc', 'docx']
img_file_formats = ['png','jpg','jpeg','gif']
video_file_formats = ['mp4', 'mkv']
programming_file_formats = ['py', 'js', 'cpp']
pdf_file_formats= ['pdf']
text_file_formats=['txt']
file_ext=[]
file_name=[]
count=1
"""
while True:
    len(files)==0:
    break
"""


for i in range(0,len(files)-1):
    #print(file)
    
    if i==0:
        get_file_index = files.index(main_file)
        del files[get_file_index]
       
    
   # file_ext =file.split(".")[-1]
    file_name.insert(0,files[i][0:files[i].index('.')])
"""
    str=""
    str=str+file_name

    del files
"""
"""
    if file_ext in audio_file_formats:
        if file_name =='mathematics':
            shutil.move(file, maths_folder_audio)
        elif file_name =='computer':
            shutil.move(file, computer_folder_audio)
        elif file_name =='science':
            shutil.move(file, science_folder_audio)
        elif file_name =='history':
            shutil.move(file, history_folder_audio)

    if file_ext in img_file_formats:
        
        if file_name == 'math':
            shutil.move(file, maths_folder_images)
            
        elif file_name == 'computer':
            shutil.move(file, computer_folder_images)
        elif file_name == 'science':
            shutil.move(file, science_folder_images)
        elif file_name == 'history':
            shutil.move(file, history_folder_images)
        exit

    if file_ext in doc_file_formats:
        shutil.move(file, document_folder)
        if file_name =='mathematics':
            shutil.move(file, maths_folder_document)
        elif file_name =='computer':
            shutil.move(file, computer_folder_document)
        elif file_name =='science':
            shutil.move(file, science_folder_document)
        elif file_name =='history':
            shutil.move(file, history_folder_document)

    if file_ext in text_file_formats:
        shutil.move(file, text_folder)
        if file_name =='mathematics':
            shutil.move(file, maths_folder_text)
        elif file_name =='computer':
            shutil.move(file, computer_folder_text)
        elif file_name =='science':
            shutil.move(file, science_folder_text)
        elif file_name =='history':
            shutil.move(file, history_folder_text)

    if file_ext in video_file_formats:
        shutil.move(file, video_folder)
        if file_name =='mathematics':
            shutil.move(file, maths_folder_video)
        elif file_name =='computer':
            shutil.move(file, computer_folder_video)
        elif file_name =='science':
            shutil.move(file, science_folder_video)
        elif file_name =='history':
            shutil.move(file, history_folder_video)

    if file_ext in programming_file_formats:
        shutil.move(file, programming_folder)
        if file_name =='mathematics':
            shutil.move(file, maths_folder_prg)
        elif file_name =='computer':
            shutil.move(file, computer_folder_prg)
        elif file_name =='science':
            shutil.move(file, science_folder_prg)
        elif file_name =='history':
            shutil.move(file, history_folder_prg)

    if file_ext in pdf_file_formats:
        shutil.move(file, pdf_folder)
        if file_name =='mathematics':
            shutil.move(file, maths_folder_pdf)
        elif file_name =='computer':
            shutil.move(file, computer_folder_pdf)
        elif file_name =='science':
            shutil.move(file, science_folder_pdf)
        elif file_name =='history':
            shutil.move(file, history_folder_pdf)
"""
print(files)
print(type(file_ext))
print(file_ext)
print(file_name)