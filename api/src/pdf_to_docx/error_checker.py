from pdf2docx import Converter
import constants

def error_check(pdfFile, start, end):
    cv = Converter(pdfFile)
    errors = []

    try:
        for i in range(int(start), int(end)):
            print(f'{constants.Colors.GREEN} [PAGE INFO] Page: {i} {constants.Colors.ENDTEXT}')

            output_stream = io.BytesIO()

            try:
                cv.convert(output_stream, start=i, end=i+1)
            except Exception as ex:
                print(f'{constants.Colors.RED} [Error]: {ex} in page {i} {constants.Colors.ENDTEXT}')
                errors.append(f'Error: {ex} in page {i}')
            finally:
                output_stream.close()

                print(constants.Colors.WARNING)

    except Exception as ex:
        print("Erro no for")
    finally:
        cv.close()
