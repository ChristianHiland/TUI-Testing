# Checking the option for installing All
if [ $4 -eq "y" ]; then
    # Going to the folder that has the JSON.zip file, and unzipping the zip file.
    cd $1 && unzip -q JSON.zip && rm JSON.zip
    # Going to the folder that has the PyKorean.zip file, and unzipping the zip file.
    cd $2 && unzip -q PyKorean.zip && rm PyKorean.zip
    # Going to the folder that has the HTMLQuiz.zip file, and unzipping the zip file.
    cd $3 && unzip -q Learning-Web.zip && rm Learning-Web.zip
else
    # Checking JSON.
    if [ $5 -eq "y"]; then
        # Going to the folder that has the JSON.zip file, and unzipping the zip file.
        cd $1 && unzip -q JSON.zip && rm JSON.zip
    fi
    if [ $6 -eq "y" ]; then
        # Going to the folder that has the PyKorean.zip file, and unzipping the zip file.
        cd $2 && unzip -q PyKorean.zip && rm PyKorean.zip
    fi
    if [ $7 -eq "y" ]; then
        # Going to the folder that has the HTMLQuiz.zip file, and unzipping the zip file.
        cd $3 && unzip -q Learning-Web.zip && rm Learning-Web.zip
    fi
fi