import pyttsx3
import PyPDF2

def pdf_to_audio(pdf_path, output_audio_path):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        
        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text()
    
    # Set properties for the voice (optional)
    engine.setProperty('rate', 150)  # Speed (words per minute)
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    
    # Save the text as audio
    engine.save_to_file(text, output_audio_path)
    engine.runAndWait()
    print(f"Audio book saved to {output_audio_path}")

# Example usage
pdf_path = 'example.pdf'  # Path to the PDF file
output_audio_path = 'audiobook.mp3'  # Path to save the audiobook
pdf_to_audio(pdf_path, output_audio_path)
