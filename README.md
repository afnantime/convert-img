# Image Converter Web Application

This web application allows users to upload images in various formats and convert them to a different format of their choice. It supports a range of image formats including JFIF, JPG, JPEG, PNG, and GIF.

## Features

- **Upload Images**: Users can upload one or multiple images for conversion.
- **Convert Images**: Supports conversion to PNG, JPG, ICO, and WEBP formats.
- **Download Converted Images**: Users can download the converted images directly from the web interface.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pillow (PIL Fork)

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:

```sh
pip install Flask Pillow
```

3. Navigate to the project directory and start the Flask application:

```sh
python app.py
```

4. Open a web browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

1. From the main page, click on the upload area or drag and drop your images.
2. Select the target format for the conversion using the dropdown menu.
3. Click the upload button to start the conversion process.
4. Once the conversion is complete, download links for the converted images will be provided.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML files for the web interface.
- `uploads/`: Default directory for uploaded and converted images.

## Contributing

Contributions to improve the project are welcome. Please follow the standard fork and pull request workflow.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Flask for the web framework.
- Pillow for handling image file conversions.
- Tailwind CSS and Preline for the frontend design.