## 📜 About This Folder
This folder contains details about the assignment 2.

### 🚀 Running the Simulations
Wanna see some atoms dance? 🕺💃 Follow these simple steps:

### 🔧 Requirements
1. 🏗️ towhee – to run and analyse the simulation files.
2. 🔬 OVITO – to visualize and analyze the results.

### 🏃‍♂️ Steps to Run
1️⃣ **Setting up Towhee** \
&emsp; Ensure that Towhee is installed and accessible from your terminal. If not, follow the official installation guide for your system.

2️⃣ **Running Towhee Simulations** \
&emsp;To execute a Towhee input file, navigate to the directory containing your input file and run:
```
towhee < towhee_input_file
```
&emsp;*(Replace towhee_input_file with the actual input filename.)*
    
3️⃣ **Analyzing Results**\
&emsp;Once the simulation is complete, use `analyse_movie` to extract useful data:\
- To get the `analyse_movie` util. Go to the `Utils` directory in the downloaded towhee directory and run:
```
make analyse_movie
```
  (this will create an executable `analyse_movie` file)
  - To obtain the **radial distribution function** (RDF):\
      steps have been attached in the image `analyse_movie_settings.png`
  - To compute **atomic distribution profiles**:\
      steps have been attached in the image `analyse_movie_distribution.png`

4️⃣ **Visualising in OVITO**\
&emsp;Load the `.pdb` file (just need to upload one file, ovito loads other files on its own!) into OVITO for visualization and analysis.
    
🎯 Happy Simulating! 💡
