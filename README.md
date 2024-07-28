# Pawsome Facts - README

## Overview

**Pawsome Facts** is a Streamlit web application that presents interesting and fun facts about cats. The app uses a SQLite database to store and retrieve cat facts, which are initially loaded from a JSON file. The application features a visually appealing interface with a custom background image, unique fonts, and styled elements to enhance the user experience.

## Features

- **Custom Background Image**: Adds a background image to the app from a local file.
- **Styled Interface**: Uses custom CSS to style the title, expanders, and fact text.
- **SQLite Database**: Stores cat facts in a SQLite database for persistent storage.
- **JSON Data Source**: Loads cat facts from a JSON file.
- **Expandable Fact Sections**: Displays cat facts in expandable sections with creative titles.


## Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)
- Streamlit
- requests
## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/zbersu/cat-facts-app.git
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Navigate to the Project Directory**
    ```bash
    cd path/to/cat-facts-app
    ```
   
4. **Activate the virtual environment**
- On Windows:
  ```
  .cat_app_venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source .cat_app_venv/bin/activate
  ```

5. **Ensure the Background Image is Present**

   Ensure you have the following files in your project directory:
- `cat_background.jpg`: The background image for the app:

## Running the App

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run main.py
```
The app will be opened in your web browser

To stop the app, press `Ctrl+C` in the terminal where it's running.

## Customization
- To change the background image, replace `cat_background.jpg` with your desired image.
- Adjust the custom CSS in the app to modify colors, fonts, or layout.

## Troubleshooting
- If you encounter any issues with missing modules, ensure you've activated the virtual environment and installed all dependencies.
- If the background image doesn't appear, check that `cat_background.jpg` is in the correct location.
- For any other issues, please check the Streamlit documentation or open an issue in the project repository.

## Contributing
Contributions to Pawsome Facts are welcome! Please feel free to submit a Pull Request.


## Acknowledgements
- Cat facts sourced from https://cat-fact.herokuapp.com/facts
- Cat GIF from GIPHY https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif
- Background image from https://pngtree.com/freepng/cat-footprints-border-cartoon-cute-roses_8994360.html

Enjoy your journey through the wonderful world of cat facts with Pawsome Facts!