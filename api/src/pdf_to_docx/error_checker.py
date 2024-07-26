from pdf2docx import Converter
from constants import colors

def error_check(pdfFile, start, end):
    cv = Converter(pdfFile)
    errors = []

    try:
        for i in range(int(start), int(end)):
            print(f'{Colors.GREEN} [PAGE INFO] Page: {i} {Colors.ENDTEXT}')

            output_stream = io.BytesIO()

            try:
                cv.convert(output_stream, start=i, end=i+1)
            except Exception as ex:
                print(f'{Colors.RED} [Error]: {ex} in page {i} {Colors.ENDTEXT}')
                errors.append(f'Error: {ex} in page {i}')
            finally:
                output_stream.close()

                print(Colors.WARNING)

    except Exception as ex:
        print("Erro no for")
    finally:
        cv.close()
