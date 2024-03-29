from src import *
import streamlit as st

def main():
    st.set_page_config(page_icon='./train.png')
    mdResString = ''
    st.markdown("""
    <style>
    .css-pxxe24 {
    visibility: hidden;
    }
    .element-container:has(#Rapid) + div div {
        justify-content:left;
        width: 350px;
        display: flex;
    }
    .element-container:has(#Rapid) + div .stNumberInput {
        justify-content:center;
        margin-left:8%;
    }
    .stButton {
        display:grid;
        justify-content:center;
    }
    button[kind="secondary"]{
        width: 125.6px;
        font-weight: semibold;
    }
    .stNumberInput {
        justify-content: center;
    }
    </style>""", unsafe_allow_html=True)

    st.caption("Train Function App")

    st.markdown("""
        <p style="font-size:24px; font-weight:bolder; font-family:monospace; text-align:center">
        Input for 4 separate numbers between 0 and 9.
        </p>
        """,unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4,gap="large")
    with st.container():
        x_1 = col1.number_input("X1",value=0, min_value=0, max_value=9, key=1, label_visibility="collapsed")
        x_2 = col2.number_input("X2",value=0, min_value=0, max_value=9, key=2, label_visibility="collapsed")
        x_3 = col3.number_input("X3",value=0, min_value=0, max_value=9, key=3, label_visibility="collapsed")
        x_4 = col4.number_input("X4",value=0, min_value=0, max_value=9, key=4, label_visibility="collapsed")
    
    x_values = [x_1,x_2,x_3,x_4]


    # Input for the target number y
    st.markdown("""
        <p style="padding-top: 2rem; font-size:24px; font-weight:bolder; font-family:monospace; text-align:center">
        Input a target number.
        </p>
        """,unsafe_allow_html=True)

    st.markdown("""<span id="Rapid"></span>""", unsafe_allow_html=True)
    target = st.number_input("""Input a goal number""", value=10,min_value=0,max_value=6561,key="goal", label_visibility="collapsed")


    x_string = f'''
    <p style="padding-top: 0.5rem; font-size:20px; font-family:monospace; text-align:center">
    Can [ {x_1}, {x_2}, {x_3}, {x_4} ]  make {target}?
    </p>'''
    # Button to trigger the train function
    if st.button("Solve",key="Btn"):
        resultStr, searchRes = run(x_values, target)
        if searchRes == None:
            result = f'This cannot be solved for a target of: {target}'
            result1 = f'''<br> '''

        else:
            result = f'''This can be solved!'''
            result1 = f'''{resultStr} = {target}'''

        mdResString = f'''<p style="padding-top: 0rem; font-size:24px; font-family:monospace; text-align:center">
        {result}
        </p>
        <p style="padding-top: 0rem; font-size:32px; font-weight:bolder; font-family:monospace; text-align:center">
        {result1}
        </p>
        '''
        x_string = f'''
        <p style="padding-top: 0.5rem; font-size:20px; font-family:monospace; text-align:center; color:lightgrey">
        Can [ {x_1}, {x_2}, {x_3}, {x_4} ]  make {target}?
        </p>'''


    st.markdown(x_string,unsafe_allow_html=True)
    st.markdown(mdResString, unsafe_allow_html=True)
    

if __name__ == "__main__":
    main()

# while __name__ == "__main__":
#     print(f'Enter the 4 digits to check (separated by a comma):\n')
#     y = input()
#     x = [int(i) for i in y.split(',')]

#     print(f'\nEnter the target number:\n')
#     goal = int(input())
#     print(f'\n\n')
#     train_game(x,goal)
#     print(f'\n')
#     time.sleep(1)
#     print('Continue (y/n)')
#     cont = input()
#     if cont.lower() != 'y':
#         break
#     time.sleep(1)
#     print(f'\n')