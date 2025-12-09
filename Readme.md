# How to use this RAG AI Teaching Assistant on your own data
## Step 1 - Collect you videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by running video_to_mp3

## Step 3 - Convert mp3 to json 
Convert all the mp3 files jsons by running mp3_to_json

## Step 4 - Convert the json files to vectors
Use the file preprocess_json to convert the json files to a dataframe with embeddings and save it as a joblib pickle

## Step 5 - Prompt Generation and feeding to LLM 
Read the Joblib file and load it into memory. Then create a relevant prompt as per the user query and feed it to the LLM. 