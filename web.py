import streamlit as st
import functions

st.title("My Todo App")

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].upper() + "\n"
    if len(todo) > 1:
        todos.append(todo)
        functions.write_todos(todos)
    else:
        functions.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        print(index)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
