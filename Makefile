# Makefile

PYTHON_SCRIPT = Main.py
SUB_SCRIPTS = Scripts/Install.py Scripts/JSONMaker.py Scripts/LearningWeb.py Scripts/PyKorean.py Scripts/Short.py Scripts/__init__.py 
OUTPUT_DIR = bin

.PHONY: all windows linux clean

all: windows linux

windows: $(OUTPUT_DIR)/$(PYTHON_SCRIPT).exe

linux: $(OUTPUT_DIR)/$(PYTHON_SCRIPT)

$(OUTPUT_DIR)/$(PYTHON_SCRIPT).exe: $(PYTHON_SCRIPT) $(SUB_SCRIPTS)
	mkdir -p $(OUTPUT_DIR)
	pyinstaller --onefile --distpath=$(OUTPUT_DIR) --name=$(PYTHON_SCRIPT) $(PYTHON_SCRIPT)

$(OUTPUT_DIR)/$(PYTHON_SCRIPT): $(PYTHON_SCRIPT) $(SUB_SCRIPTS)
	mkdir -p $(OUTPUT_DIR)
	cp $(PYTHON_SCRIPT) $(OUTPUT_DIR)/$(PYTHON_SCRIPT)
	cp $(SUB_SCRIPTS) $(OUTPUT_DIR)
	chmod +x $(OUTPUT_DIR)/$(PYTHON_SCRIPT)

clean:
	rm -rf $(OUTPUT_DIR)
	rm -f Main.spec
	rm -f Main.py.spec
	rm -r dist
cleanall:
	rm -rf $(OUTPUT_DIR)
	rm -f Main.spec
	rm -f Main.py.spec
	rm -r dist
	rm -rf build
