import re
import subprocess  # noqa: S404
import doc_2_txt
import pdf__miner


PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')


def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) <= 16:
            return number
    return None


if __name__ == '__main__':

    text = pdf__miner.extract_text_from_pdf('resume2.pdf')
    phone_number = extract_phone_number(text)

    print(phone_number)
