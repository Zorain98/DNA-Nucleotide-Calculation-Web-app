import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt

st.set_page_config(page_title="DNA Nucleotide Count Web App", page_icon="🧬", layout='wide')
image = Image.open('dna_pic.png')
st.image(image, use_container_width=False, width=150)
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
***
""")

# Input text box
st.header('Enter DNA sequence')
sequence_input = "agagggcttaccataattttcagggcaatcagatccatcgaggcgggtggtccctcaaaatgactatgttctagggcgtgcagctagccggttcttttggggtggttctt"
sequence = st.text_area("Sequence input", sequence_input, height=250)

st.write("""
***
""")

# Print the DNA sequence
st.header('Input DNA sequence')
sequence

# DNA nucleotide count
st.header('Output DNA Nucleotide Count')

# 1. Print dictionary
st.subheader('Count of Nucleotides')
def dna_nucleotide_count(seq):
    d = dict([
        ("a", seq.count("a")),
        ("t", seq.count("t")),
        ("g", seq.count("g")),
        ("c", seq.count("c"))
        ])
    return d

X = dna_nucleotide_count(sequence)
X

st.write("""
***
""")

# 2. Print text
st.subheader('Description')
st.write('There are ' + str(X['a']) + ' adenine (a)')
st.write('There are ' + str(X['t']) + ' thymine (t)')
st.write('There are ' + str(X['g']) + ' guanine (g)')
st.write('There are ' + str(X['c']) + ' cytosine (c)')

st.write("""
***
""")

# 3. Display DataFrame
st.subheader('DataFrame')
df=pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.write("""
***
""")

# 4. Bar Chart
st.subheader('Bar Chart')

plot = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
plot = plot.properties(
    width=alt.Step(80)
)
st.write(plot)

