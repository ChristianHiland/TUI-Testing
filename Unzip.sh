# Going to the folder that has the JSON.zip file, and unzipping the zip file.
cd $1 && unzip -q JSON.zip && rm JSON.zip
# Going to the folder that has the PyKorean.zip file, and unzipping the zip file.
cd $2 && unzip -q PyKorean.zip && rm PyKorean.zip
# Going to the folder that has the HTMLQuiz.zip file, and unzipping the zip file.
cd $3 && unzip -q HTMLQuiz.zip && rm HTMLQuiz.zip