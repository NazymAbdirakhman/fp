import os
from docx2pdf import convert

def convert_docx_to_pdf(docx_file, pdf_file):
    """
    Конвертирует файл .docx в файл .pdf.

    :param docx_file: Путь к исходному файлу .docx.
    :param pdf_file: Путь, по которому будет сохранен PDF-файл.
    """
    try:
        convert(docx_file, pdf_file)
        print("Конвертация завершена успешно!")
    except Exception as e:
        print(f"Произошла ошибка при конвертации: {e}")

def get_project_folder():
    """
    Получает текущую директорию проекта.
    """
    return os.path.dirname(os.path.abspath(__file__))

def get_file_paths(project_folder):
    """
    Формирует пути к файлам "naz.docx" и "output.pdf".
    """
    docx_file = os.path.join(project_folder, "naz.docx")
    pdf_file = os.path.join(project_folder, "output.pdf")
    return docx_file, pdf_file

def main():
    """
    Основная функция программы.
    """
    project_folder = get_project_folder()
    docx_file, pdf_file = get_file_paths(project_folder)
    convert_docx_to_pdf(docx_file, pdf_file)

if __name__ == "__main__":
    main()
