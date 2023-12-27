#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    main.py.py
# @Author:      ikbal
# @Time:        12/27/2023 10:12 PM

import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="SAU AI Education",
    page_icon=":sparkles:",
    layout="wide",
)


# Sidebar
page = st.sidebar.radio("", ["General Applications", "Code Hub"])
st.sidebar.markdown("---")


