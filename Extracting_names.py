
import doc_2_txt
import file_selection
import pdf__miner
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0]
                             for chunk_leave in chunk.leaves())
                )

    return person_names


if __name__ == '__main__':

    File_type_num = int(
        input(print("Resume's File Type: Press 1 for DOCX \n\tPress 2 for PDF")))
    if File_type_num == 1:
        text = doc_2_txt.extract_text_from_docx('resume1.docx')
    elif File_type_num == 2:
        text = pdf__miner.extract_text_from_pdf("resume2.pdf")
    else:
        print("invalid option")
        pass

    '''file_selection.select_FILE_TYPE()'''
    names = extract_names(text)
    if names:
        print(names[0])
