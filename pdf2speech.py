import PyPDF2
import pyttsx3

def read_and_speak_pdf(pdf_file_path):
    """Reads text from a PDF file and converts it to speech using pyttsx3.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Raises:
        FileNotFoundError: If the PDF file is not found.
        ValueError: If the PDF file is password-protected or cannot be read.
        RuntimeError: If an error occurs during text extraction or speech synthesis.
    """

    try:
        # Open the PDF file in binary read mode
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Check if the PDF is password-protected
            if pdf_reader.isEncrypted:
                raise ValueError("PDF file is password-protected. Please remove the password.")

            # Iterate through each page of the PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]

                # Extract text from the page using appropriate methods
                text = page.extract_text()

                # Create a pyttsx3 engine and set voice properties
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[0].id)  # Set default voice

                # Speak the extracted text
                engine.say(text)
                engine.runAndWait()

    except FileNotFoundError as e:
        print(f"Error: PDF file '{pdf_file_path}' not found.")
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
    finally:
        # Close the engine to avoid memory leaks
        engine.stop()


if __name__ == '__main__':
    # Get the PDF file path from the user
    pdf_file_path = input("Enter the path to your PDF file: ")

    # Read the PDF and speak the text
    read_and_speak_pdf(pdf_file_path)
