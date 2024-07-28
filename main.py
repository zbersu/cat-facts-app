import json
import sqlite3
import streamlit as st
import base64

# Function to add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

# Set page config
st.set_page_config(page_title="Pawsome Facts", page_icon=":heart_eyes_cat:", layout="wide")

# Add background image
add_bg_from_local('cat_background.jpg')

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    h1 {
        font-family: 'Pacifico', cursive;
        color: #FF6B6B;
        text-align: center;
        font-size: 50px;
        text-shadow: 2px 2px 4px #000000;
        margin-top: 20px;
    }
    .stExpander {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .stExpanderHeader {
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        color: #4A4A4A;
    }
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .title-container img {
        margin-left: 20px;
    }
    .fact-text {
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title with centered alignment
st.markdown("<h1>Pawsome Facts</h1>", unsafe_allow_html=True)

# Database functions
def create_database():
    """Create SQLite database and table if not exists"""
    conn = sqlite3.connect('cat_facts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS facts (
            id TEXT PRIMARY KEY,
            text TEXT
        )
    ''')
    conn.commit()
    return conn

def fetch_cat_facts():
    """Fetch cat facts from JSON file"""
    try:
        with open('cat_facts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("Error: cat_facts.json file not found.")
        return None
    except json.JSONDecodeError:
        st.error("Error: Invalid JSON in cat_facts.json file.")
        return None

def save_facts_to_db(conn, facts):
    """Save facts to the database"""
    cursor = conn.cursor()
    for fact in facts:
        cursor.execute('''
            INSERT OR REPLACE INTO facts (id, text)
            VALUES (?, ?)
        ''', (
            fact['_id'],
            fact['text']
        ))
    conn.commit()

def get_facts_from_db(conn):
    """Retrieve facts from the database"""
    cursor = conn.cursor()
    cursor.execute('SELECT text FROM facts')
    return cursor.fetchall()

def main():
    """Main function to run the Streamlit app"""
    conn = create_database()
    facts = fetch_cat_facts()
    if facts:
        save_facts_to_db(conn, facts)
    db_facts = get_facts_from_db(conn)

    titles = [
        "**🧡 Purr-fect for Your Heart**",
        "**🥛 Milk-Free Meow: The Truth About Cats and Dairy**",
        "**😴 Cat Nap Champions: The Ultimate Sleepers**",
        "**🎵 Nature's Healer: The Power of a Cat's Purr**",
        "**🐾 America's Feline Obsession: Cats Rule!**"
    ]

    if db_facts:
        for i, (fact, title) in enumerate(zip(db_facts, titles)):
            if i == len(db_facts) - 1:  # Last fact
                with st.expander(f"{title} "):
                    st.markdown(f'<p class="fact-text">{fact[0]}</p>', unsafe_allow_html=True)
            else:
                with st.expander(title):
                    st.markdown(f'<p class="fact-text">{fact[0]}</p>', unsafe_allow_html=True)
    else:
        st.warning("No facts found in the database.")

    conn.close()

if __name__ == "__main__":
    main()

# Add a fun cat gif at the bottom
st.markdown("![Cat GIF](https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif)")