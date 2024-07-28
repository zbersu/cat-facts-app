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
## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/zbersu/cat-facts-app.git
    cd cat-facts-app
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure JSON File and the Background Image is Present**

   Ensure you have the following files in your project directory:
- `cat_facts.json`: A JSON file containing cat facts
- `cat_background.jpg`: The background image for the app:

## Running the App

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run main.py
```

The app will be opened in your web browser

## Customization
- To change the background image, replace `cat_background.jpg` with your desired image.
- Adjust the custom CSS in the app to modify colors, fonts, or layout.

## Acknowledgements
- Cat facts sourced from https://cat-fact.herokuapp.com/facts
- Cat GIF from GIPHY https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif
- Background image from https://pngtree.com/freepng/cat-footprints-border-cartoon-cute-roses_8994360.html

Enjoy your journey through the wonderful world of cat facts with Pawsome Facts!