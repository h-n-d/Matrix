/* Matrix Theme CSS */
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

/* Global Styles */
html, body {
    height: 100%;
    margin: 0;
    padding: 0;
}

.stApp {
    background-color: #000000;
    background-image: 
        linear-gradient(0deg, rgba(0, 20, 0, 0.9) 0%,
                             rgba(0, 0, 0, 0.9) 100%);
    font-family: 'Share Tech Mono', monospace;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
}

/* Title and Headers */
.stTitle {
    color: #00ff00 !important;
    text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
    text-align: center;
    font-size: 3em !important;
    margin-bottom: 2rem;
    animation: glow 1.5s ease-in-out infinite alternate;
}

/* Buttons */
.stButton > button {
    background-color: transparent !important;
    color: #00ff00 !important;
    border: 2px solid #00ff00 !important;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    transition: all 0.3s ease;
    text-shadow: 0 0 5px #00ff00;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
}

.stButton > button:hover {
    background-color: rgba(0, 255, 0, 0.1) !important;
    box-shadow: 0 0 20px rgba(0, 255, 0, 0.4);
    transform: scale(1.05);
}



/* Text Elements */
.stMarkdown {
    color: #cccccc !important;
}

/* DataFrames and Tables */
.dataframe {
    background-color: rgba(0, 20, 0, 0.3) !important;
    border: 1px solid rgba(0, 255, 0, 0.2) !important;
    border-radius: 5px;
}

.dataframe th {
    background-color: rgba(0, 255, 0, 0.1) !important;
    color: #00ff00 !important;
    text-shadow: 0 0 5px #00ff00;
}

.dataframe td {
    color: #ffffff !important;
}

/* File Uploader */
.stFileUploader {
    background-color: rgba(0, 20, 0, 0.3) !important;
    border: 2px dashed #00ff00 !important;
    border-radius: 5px;
    padding: 1rem;
    transition: all 0.3s ease;
}

.stFileUploader:hover {
    background-color: rgba(0, 255, 0, 0.1) !important;
    box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
}

/* Select Boxes */
.stSelectbox > div > div {
    background-color: rgba(0, 20, 0, 0.3) !important;
    border: 1px solid #00ff00 !important;
    color: #00ff00 !important;
}

/* Radio Buttons */
.stRadio > div {
    background-color: transparent !important;
    color: #00ff00 !important;
}

/* Animations */
@keyframes glow {
    from {
        text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 15px #00ff00;
    }
    to {
        text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
    }
}

/* Matrix Rain Animation */
.matrix-rain {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
}

/* Footer */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: rgba(0, 20, 0, 0.8);
    padding: 1rem;
    text-align: center;
    border-top: 1px solid #00ff00;
    box-shadow: 0 -5px 15px rgba(0, 255, 0, 0.1);
}

.footer a {
    color: #00ff00;
    text-decoration: none;
    margin: 0 1rem;
    transition: all 0.3s ease;
}

.footer a:hover {
    text-shadow: 0 0 10px #00ff00;
}
