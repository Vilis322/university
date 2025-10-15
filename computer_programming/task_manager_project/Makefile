# Simple cross-platform Makefile for task_manager

PKG = task_manager
MOD = $(PKG).main

HOST_PY := $(if $(shell command -v python3 2>/dev/null),python3,python)

define VENV_RUN
sh -c 'PY=$$( [ -x .venv/bin/python ] && echo .venv/bin/python || echo .venv/Scripts/python.exe ); \
       "$$PY" $(1)'
endef

define RUN_CLI
sh -c 'if [ -x .venv/bin/taskman ]; then BIN=.venv/bin/taskman; \
      elif [ -x .venv/Scripts/taskman.exe ]; then BIN=.venv/Scripts/taskman.exe; \
      else PY=$$( [ -x .venv/bin/python ] && echo .venv/bin/python || echo .venv/Scripts/python.exe ); \
           BIN="$$PY -m $(MOD)"; \
      fi; \
      $$BIN $(1)'
endef

SIZE  ?= 20
MIN   ?= 0
MAX   ?= 10
SEED  ?= 42
COUNT ?= 5
ifdef size
override SIZE := $(size)
endif
ifdef min
override MIN := $(min)
endif
ifdef max
override MAX := $(max)
endif
ifdef seed
override SEED := $(seed)
endif
ifdef count
override COUNT := $(count)
endif

.PHONY: help venv install reinstall clean task1 task2 task3 task4 task5 test cov

help:
	@echo "Usage:"
	@echo "  make venv              # create .venv (idempotent) and upgrade pip"
	@echo "  make install           # install deps + install package (editable)"
	@echo "  make reinstall         # force re-install deps and package"
	@echo "  make clean             # remove .venv (full reset)"
	@echo ""
	@echo "Tasks:"
	@echo "  make task1 [size=20] [min=0] [max=10] [seed=42]"
	@echo "  make task2"
	@echo "  make task3"
	@echo "  make task4"
	@echo "  make task5 [count=5]"
	@echo ""
	@echo "Tests:"
	@echo "  make test              # pytest with prints and verbose"
	@echo "  make cov               # pytest with coverage summary"
	@echo ""
	@echo "Notes: lowercase args override defaults, e.g., make task1 size=30"

venv:
	@if [ ! -d ".venv" ]; then \
	  echo "Creating venv with $(HOST_PY)"; \
	  $(HOST_PY) -m venv .venv || python -m venv .venv; \
	fi
	@$(call VENV_RUN,-m pip install -U pip)

install: venv
	@$(call VENV_RUN,-m pip install -r requirements.txt)
	@$(call VENV_RUN,-m pip install -e .)
	@$(call VENV_RUN,-c "import sys; print('Installed to:', sys.executable)")
	@echo "Install complete."

reinstall: venv
	@$(call VENV_RUN,-m pip install -U -r requirements.txt)
	@$(call VENV_RUN,-m pip install -e . --force-reinstall)
	@echo "Force reinstalled."

clean:
	@$(HOST_PY) -c "import shutil; shutil.rmtree('.venv', ignore_errors=True)"
	@echo "Removed .venv"

# Tasks
task1:
	@$(call RUN_CLI,task1 --size $(SIZE) --min $(MIN) --max $(MAX) --seed $(SEED))

task2:
	@$(call RUN_CLI,task2)

task3:
	@$(call RUN_CLI,task3)

task4:
	@$(call RUN_CLI,task4)

task5:
	@$(call RUN_CLI,task5 --count $(COUNT))

# Tests
test:
	@$(call VENV_RUN,-m pytest -s -vv -rA)

cov:
	@$(call VENV_RUN,-m pytest -s -vv -rA --maxfail=1 --disable-warnings --cov=$(PKG) --cov-report=term-missing)
