cd Installed
if [ $1 == "Y" ];
then
# Unzipping JSON into the JSON folder in the installed folder.
mkdir JSON
unzip -d JSON/ JSON.zip
rm JSON.zip
# Unzipping PyKorean into the PyKorean folder in the isntalled folder.
mkdir PyKorean
unzip -d PyKorean/ PyKorean.zip
rm PyKorean.zip
fi