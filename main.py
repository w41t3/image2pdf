from tkinter import filedialog
import img2pdf
import os


def convert_image_to_pdf(file_path):
    try:
        if not file_path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("Неверный формат файла. Пожалуйста, выберите JPG или JPEG.")

        with open(file_path, 'rb') as image_file:
            pdf = img2pdf.convert(image_file)

        output_filename = f"{os.path.splitext(file_path)[0]}.pdf"
        with open(output_filename, "wb") as f:
            f.write(pdf)

        print(f"Файл {output_filename} успешно сохранен!")

    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")


def select_images():
    files = filedialog.askopenfilenames(title="Выберите изображения", filetypes=(("Image files", "*.jpg;*.jpeg"),))
    for file in files:
        convert_image_to_pdf(file)


select_images()
