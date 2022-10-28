import doc_2_txt
import pdf__miner


def select_FILE_TYPE():
    File_type_num = int(input(
        print("Resume's File Type: Press 1 for DOCX \n\t            Press 2 for PDF")))

    if File_type_num == 1:
        text = doc_2_txt.extract_text_from_docx('resume1.docx')
    elif File_type_num == 2:
        text = pdf__miner.extract_text_from_pdf("resume2.pdf")
    else:
        print("invalid option")
    return text
