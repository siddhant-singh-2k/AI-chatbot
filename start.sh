#!/bin/bash

# Run backend on port 9999
python backend.py &

# Run Streamlit frontend
streamlit run frontend.py --server.port 8501